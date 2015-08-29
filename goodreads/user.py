import goodreads as gr


class GoodreadsUser(object):
    def __init__(self, user_dict, client):
        self._user_dict = user_dict
        self._client = client   # for later queries
        self._shelves = None
        self._owned_books = None
        self._groups = None

    def __repr__(self):
        return self.user_name  # TODO: Decode! probably at request level (?)

    @property
    def gid(self):
        """Goodreads ID for the user"""
        return self._user_dict['id']

    @property
    def user_name(self):
        """Goodreads handle of the user"""
        return self._user_dict['user_name']

    @property
    def name(self):
        """Name of the user"""
        return self._user_dict['name']

    @property
    def link(self):
        """URL for user profile"""
        return self._user_dict['link']

    @property
    def image_url(self):
        """URL of user image"""
        return self._user_dict['image_url']

    @property
    def small_image_url(self):
        """URL of user image (small)"""
        return self._user_dict['small_image_url']

    @property
    def groups(self):
        """List groups for the user."""
        if self._groups is None:
            resp = self._client.request_all_pages("group/list/%s.xml" % self.gid, {},
                                                  list_key=('groups', 'list'), item_key='group')
            self._groups = [gr.Group(g) for g in resp]
        return self._groups

    @property
    def owned_books(self):
        """Return the list of books owned by the user"""
        if self.owned_books is None:
            resp = self._client.request_all_pages("owned_books/user/%s.xml" % self.gid, {'format': 'xml'},
                                                  oauth=True, list_key='owned_books', item_key='owned_book')
            self._owned_books = [gr.OwnedBook(d) for d in resp]
        return self._owned_books

    @property
    def reviews(self):
        """Get all reviews on user's shelves"""
        return sum((s.reviews for s in self.shelves), [])

    @property
    def shelves(self):
        """Get the user's shelves."""
        if self._shelves is None:
            resp = self._client.request_all_pages("shelf/list.xml", {'user_id': self.gid},
                                                  list_key='shelves', item_key='user_shelf', oauth=True)
            self._shelves = [gr.Shelf(d, self, self._client) for d in resp]
        return self._shelves
