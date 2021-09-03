from securityscorecard_api.utils.utils import url_builder

class Events(object):

    def get_events_history(self, scorecard_identifier):
        ep = f"/companies/{scorecard_identifier}/history/events"
        return self._perform_get(url_builder(ep))

    def get_events_breaches(self, scorecard_identfier):
        ep = f"/companies/{scorecard_identfier}/history/events/breaches"
        return self._perform_get(url_builder(ep))