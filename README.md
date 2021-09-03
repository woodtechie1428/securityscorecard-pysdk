# securityscorecard_api

A python SDK for interacting with the SecurityScorecard API

## Example 

```
from securityscorecard_api.client import SecurityScorecardClient

ssc = SecurityScorecardClient("your_api_token")

ssc.get_score('company.com')

```

