"""Class implementation for Goodreads reviews"""

import goodreads as gr


class GoodreadsReview(object):
    def __init__(self, review_dict, client):
        self._review_dict = review_dict
        self._client = client
        self._book = None

    def __repr__(self):
        return "review [%s]" % self.gid

    def _edit_review(self, params):
        resp = self._client.request('review/{}.xml'.format(self.gid),
                                    params=params, oauth=True, method='PUT')
        # the structure of the returned xml is different
        resp = resp['review']
        for k in resp:
            if resp[k] and '#text' in resp[k]:
                resp[k] = resp[k]['#text']
        # for some reason in the  data returned when editing a review
        # underscores are replaced by dashes in property names
        resp = {k.replace('-', '_'): v for k, v in resp.items()}
        self._review_dict.update(resp)

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

    @rating.setter
    def rating(self, value):
        """Edit rating of the book"""
        self._edit_review({'review[rating]': value})

    @property
    def shelves(self):
        """Shelves for the book"""
        if not isinstance(self._review_dict['shelves']['shelf'], list):
            return [self._review_dict['shelves']['shelf']['@name']]
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

    @read_at.setter
    def read_at(self, value):
        """Edit book read_at date"""
        self._edit_review({'review[read_at]': value})

    @property
    def body(self):
        """Body for the review"""
        return self._review_dict['body']

    @body.setter
    def body(self, value):
        """Edit review body"""
        self._edit_review({'review[review]': value})

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

