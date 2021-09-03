
from securityscorecard_api.utils.utils import url_builder

class Scores():

    def get_score(self, scorecard_identifier):
        ep = f"/companies/{scorecard_identifier}"
        url = url_builder(ep)
        return self._perform_get(url)

    def get_historical_scores(self, scorecard_identifier):
        ep = f"/companies/{scorecard_identifier}/history/score"
        return self._perform_get(url_builder(ep))

    def get_factors(self, scorecard_identifier):
        ep = f"/companies/{scorecard_identifier}/factors"
        url = url_builder(ep)
        return self._perform_get(url)

    def get_historical_factors(self, scorecard_identifier):
        ep = f"/companies/{scorecard_identifier}/history/factors/score"
        return self._perform_get(url_builder(ep))

    def get_scoreplan_by_score_target(self, domain, score):
        if (isinstance(score, int)):
            score = str(score)
        ep = f"/companies/{domain}/score-plans/by-target/{score}"
        return self._perform_get(url_builder(ep))

    def get_industry_score(self, industry):
        ep = f"/industries/{industry}/score"
        return self._perform_get(url_builder(ep))

    def get_industry_factors(self, industry):
        ep = f"/industries/{industry}/factors"
        return self._perform_get(url_builder(ep))

    def get_industry_historical_factors(self, industry):
        ep = f"/industries/{industry}/history/factors"
        return self._perform_get(url_builder(ep))

