
from requests.sessions import session
from securityscorecard_api.compliance import Compliance
from securityscorecard_api.events import Events
from securityscorecard_api.scores import Scores


class SecurityScorecardClient(Scores, Events, Compliance):
    '''
        Primary Client Class 
    '''
    def __init__(self, api_token) -> None:
        self.session = session()
        self.session.headers = {
            "Accept": "application/json; charset=utf-8",
            "Authorization": "Token "+ api_token
        }

    def _perform_get(self, api_url):
        response = self.session.get(api_url, verify=False)
        return (response.json())
