import requests

class _Util(object):
    def perform_get(self, api_url):
        response = self.session.get(api_url)
        return (response.json())