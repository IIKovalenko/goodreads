"""Class implementation for Goodreads reviews"""

import goodreads as gr


class GoodreadsReview(object):
    def __init__(self, review_dict, client):
        self._review_dict = review_dict
        self._client = client
        self._book = None

    def __repr__(self):
        return "review [%s]" % self.gid

    @property
    def gid(self):
        """Goodreads id for the review"""
        return self._review_dict['id']

    @property
    def book(self):
        """Book that the review belongs to"""
        if self._book is None:
            self._book = gr.Book(self._review_dict['book'], self._client)
        return self._book

    @property
    def rating(self):
        """Rating of the book"""
        return self._review_dict['rating']

    @property
    def shelves(self):
        """Shelves for the book"""
        return [shelf['@name']
                for shelf in self._review_dict['shelves']['shelf']]

    @property
    def recommended_for(self):
        """Book recommended for"""
        return self._review_dict['recommended_for']

    @property
    def recommended_by(self):
        """Book recommended by"""
        return self._review_dict['recommended_by']

    @property
    def started_at(self):
        """Book started at"""
        return self._review_dict['started_at']

    @property
    def read_at(self):
        """Book read at"""
        return self._review_dict['read_at']

    @property
    def body(self):
        """Body for the review"""
        return self._review_dict['body']

    @property
    def comments_count(self):
        """Number of comments to this review"""
        return self._review_dict['comments_count']

    @property
    def url(self):
        """URL for this comment"""
        return self._review_dict['url']

    @property
    def owned(self):
        """Is the book owned by this user?"""
        return self._review_dict['owned']

