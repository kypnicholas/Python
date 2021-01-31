import requests
from requests.models import Response
import json

API_KEY = 'fbfa3acebca7f8eacfa177409858f581'
USER_AGENT = 'kypick'
ENDPOINT_URL = 'http://ws.audioscrobbler.com/2.0/'

### INITIAL IMPLEMENTATION. NOT USING FUNCTIONS ### 
# headers = {
#     'user-agent': USER_AGENT
# }

# req_payload = {
#     'api_key': API_KEY,
#     'method': 'chart.gettopartists',
#     'format': 'json'
# }

# response = requests.get(ENDPOINT_URL, headers=headers, params=req_payload)

# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(response.status_code)

### USING FUNCTIONS ### 
def lastfm_get(req_payload):
    headers = {'user-agent': USER_AGENT}
    ENDPOINT_URL = 'http://ws.audioscrobbler.com/2.0/'
    
    req_payload['api_key'] = API_KEY
    req_payload['format'] = 'json'

    f_response = requests.get(ENDPOINT_URL, headers=headers, params=req_payload)
    return f_response


response = lastfm_get({'method': 'chart.gettopartists'})

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.status_code)
jprint(response.json())
