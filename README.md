# securityscorecard_api

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

