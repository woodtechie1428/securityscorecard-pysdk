
from requests.api import request
from requests.sessions import session
from securityscorecard_api.scores import Scores
from securityscorecard_api._util import _Util


class SecurityScorecardClient(Scores, _Util):
    '''
        Primary Client Class 
    '''
    def __init__(self, api_token) -> None:
        self.session = session()
        self.session.headers = {
            "Accept": "application/json; charset=utf-8",
            "Authorization": "Token "+ api_token
        }