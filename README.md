# securityscorecard_api

[![Actions Status](https://img.shields.io/github/workflow/status/woodtechie1428/securityscorecard-pysdk/Publish%20Python%20%F0%9F%90%8D%20distributions%20%F0%9F%93%A6%20to%20PyPI?style=plastic)](https://github.com/woodtechie1428/securityscorecard-pysdk/actions)
[![License](https://img.shields.io/github/license/woodtechie1428/securityscorecard-pysdk?style=plastic)](https://github.com/woodtechie1428/securityscorecard-pysdk/blob/main/LICENSE)
[![Docss](https://img.shields.io/readthedocs/securityscorecard-pysdk?style=plastic)](https://securityscorecard-pysdk.readthedocs.io/en/latest/)
[![Downlaods](https://img.shields.io/pypi/dm/securityscorecard-api?style=plastic)](https://pypi.org/project/securityscorecard-api/)
[![Version](https://img.shields.io/github/v/release/woodtechie1428/securityscorecard-pysdk?sort=semver&style=plastic)](https://github.com/woodtechie1428/securityscorecard-pysdk/releases)
[![release date](https://img.shields.io/github/release-date/woodtechie1428/securityscorecard-pysdk?style=plastic)](https://github.com/woodtechie1428/securityscorecard-pysdk/releases)

A python SDK for interacting with the SecurityScorecard API


## Installation
```
python -m pip install securityscorecard_api
```

## Example 

```
from securityscorecard_api.client import SecurityScorecardClient

ssc = SecurityScorecardClient("your_api_token")

ssc.get_score('company.com')

```

