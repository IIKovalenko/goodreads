import goodreads as gr


class GoodreadsAuthor(object):
    def __init__(self, author_dict, client, reload=False):
        self._author_dict = author_dict
        self._client = client
        if reload:
            self._author_dict = client.request("author/show",
                                               {'id': self.gid})['author']

    def __repr__(self):
        return self.name

    def _get_attr(self, attr):
        """reloads the author data if an attribute is not available

           The author data returned in e.g. a book query is not complete,
           this reloads it with a separate query if necessary.
        """
        if attr not in self._author_dict:
            self._author_dict = self._client.request("author/show", {'id': self.gid})['author']
        return self._author_dict.get(attr, None)

    @property
    def gid(self):
        """Goodreads id of the author"""
        return self._get_attr('id')

    @property
    def name(self):
        """Author name"""
        return self._get_attr('name')

    @property
    def role(self):
        """Author role"""
        return self._get_attr('role')

    @property
    def about(self):
        """About the author"""
        return self._get_attr('about')

    @property
    def books(self):
        """Books of the author"""
        # Goodreads API returns a list if there are more than one books, otherwise,
        # just the OrderedDict.
        if type(self._get_attr('books')['book']) == list:
            return [gr.Book(book_dict, self._client)
                    for book_dict in self._get_attr('books')['book']]
        else:
            return [gr.Book(self._get_attr('books')['book'],
                                      self._client)]

    @property
    def born_at(self):
        """Author date of birth"""
        return self._get_attr('born_at')

    @property
    def died_at(self):
        """Author date of death"""
        return self._get_attr('died_at')

    @property
    def fans_count(self):
        """Number of fans"""
        return self._get_attr('fans_count')

    @property
    def gender(self):
        """Author gender"""
        return self._get_attr('gender')

    @property
    def hometown(self):
        """Author's hometown"""
        return self._get_attr('hometown')

    @property
    def link(self):
        """Link for author page"""
        return self._get_attr('link')

    @property
    def image_url(self):
        """Image URL"""
        return self._get_attr('image_url')

    @property
    def small_image_url(self):
        """Small image URL"""
        return self._get_attr('small_image_url')

    @property
    def influences(self):
        """Influenced by"""
        return self._get_attr('influences')

    @property
    def user(self):
        """Goodreads user profile of the author"""
        goodreads_user = None
        if self._get_attr('user') is not None:
            goodreads_user = gr.User(
                self._get_attr('user')['id']['#text'], self._client)
        return goodreads_user

    @property
    def works_count(self):
        """Author number of works"""
        return self._get_attr('works_count')
