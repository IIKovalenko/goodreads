"""Goodreads shelf class"""

import goodreads as gr


class GoodreadsShelf:
    def __init__(self, shelf_dict, user, client):
        self._shelf_dict = shelf_dict
        self._user = user
        self._client = client
        self._reviews = None

    def __repr__(self):
        return self.name

    @property
    def reviews(self):
        """Reviews on the shelf"""
        if self._reviews is None:
            params = {'v': 2, 'per_page': 200, 'id': self.user.gid, 'shelf': self.name}
            review_data = self._client.request_all_pages(path="review/list.xml", params=params,
                                                         list_key='reviews', item_key='review', oauth=True)
            self._reviews = [gr.Review(d, self._client) for d in review_data]

        return self._reviews

    @property
    def user(self):
        """User owning this shelf"""
        return self._user

    @property
    def gid(self):
        """Goodreads id of the shelf"""
        return self._shelf_dict['id']

    @property
    def name(self):
        """Name of the shelf"""
        return self._shelf_dict['name']

    @property
    def book_count(self):
        """Number of books on the shelf"""
        return self._shelf_dict['book_count']

    @property
    def exclusive_flag(self):
        """"""
        return self._shelf_dict['exclusive_flag']

    @property
    def description(self):
        """"""
        return self._shelf_dict['description']

    @property
    def sort(self):
        """"""
        return self._shelf_dict['sort']

    @property
    def order(self):
        """"""
        return self._shelf_dict['order']

    @property
    def per_page(self):
        """Number of books returned per page"""
        return self._shelf_dict['per_page']

    @property
    def display_fields(self):
        """"""
        return self._shelf_dict['display_fields']

    @property
    def featured(self):
        """"""
        return self._shelf_dict['featured']

    @property
    def recommend_for(self):
        """"""
        return self._shelf_dict['recommend_for']

    @property
    def sticky(self):
        """"""
        return self._shelf_dict['sticky']
