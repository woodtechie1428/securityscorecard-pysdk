from securityscorecard_api.utils.utils import url_builder

class Compliance(object):

    def get_compliance_frameworks(self):
        ep = f"/compliance-frameworks"
        return self._perform_get(url_builder(ep))

    def get_compliance_frameworks_details(self, key):
        ep = f"/compliance-frameworks/{key}"
        return self._perform_get(url_builder(ep))