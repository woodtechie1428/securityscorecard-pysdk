import requests

BASE_URL = "https://api.securityscorecard.io/companies/"

class Scores():

    def get_score(self, scorecard_identifier):
        url_suffix = ""
        return self.perform_get(BASE_URL+scorecard_identifier+url_suffix)

    def get_historical_scores(self, scorecard_identifier):
        url_suffix = "/history/score"
        return self.perform_get(BASE_URL+scorecard_identifier+url_suffix)

    def get_factors(self, scorecard_identifier):
        url_suffix = "/factors"
        return self.perform_get(BASE_URL+scorecard_identifier+url_suffix)

    def get_historical_factors(self, scorecard_identifier):
        url_suffix = "/history/factors/score"
        return self.perform_get(BASE_URL+scorecard_identifier+url_suffix)

    def get_scoreplan_by_score_target(self, domain, score):
        if (isinstance(score, int)):
            score = str(score)
        url_suffix = domain+"/score-plans/by-target/"+score
        return self.perform_get(BASE_URL+url_suffix)