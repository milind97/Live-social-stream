import json
import facebook
import requests

parameters = {'access_token': 'EAAEze9xMBS0BAAArwyUOqRXQVH2QIMMKzPkuxL3JB9TiB4zQvQZCZAWlOzCBSx0kzntqRzyoLhmE5Ro76qC24Gv01X8Bcglul0BZCCu3zyrMuFvWj2nOsMONlRdwe6FqtlrPckwsml76pAEZBWuAocV6d8nDpqxxpZCwzZClpNQl7u1CG0ZBmcLORP6BZB02ZCB4VUSyE6VVySwZDZD'}
r = requests.get('https://graph.facebook.com/wittyfeedIndia/feed', params=parameters)
result = json.loads(r.text)
print(result)