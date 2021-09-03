from securityscorecard_api._defaults import BASE_URL

def url_builder(endpoint, queryparams=None):
    # BASE_URL = 'https://api.securityscorecard.io'
    url = BASE_URL + endpoint
    return url