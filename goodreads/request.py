import requests
import xmltodict
import json


class GoodreadsRequestException(Exception):
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return "{}: {}".format(self.url, self.error_msg)


class GoodreadsRequest():
    def __init__(self, client, path, query_dict, oauth=False, req_format='xml', method='GET'):
        """Initialize request object."""
        self.client = client
        self.params = query_dict.copy()
        self.params.update(client.query_dict)
        self.host = client.base_url
        self.path = path
        self.oauth = oauth
        self.req_format = req_format
        self.method = method

    def request(self):
        if self.oauth:
            resp = self.client.session.request(self.host+self.path, params=self.params)
        else:
            resp = requests.get(self.host+self.path, params=self.params)
        if resp.status_code != 200:
            raise GoodreadsRequestException(resp.reason, self.path)
        if self.req_format == 'xml':
            data_dict = xmltodict.parse(resp.text)
            return data_dict['GoodreadsResponse']
        elif self.req_format == 'json':
            return json.loads(resp.text)
        else:
            raise Exception("Invalid format")
