import requests
from requests.models import Response
import json
from datetime import datetime

response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

### to only get one element of the json object ### 
pass_times = response.json()['response']
jprint(pass_times)


#### use a loop to extract just the five 'risetime' values ###
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

jprint(risetimes)

### datetime formatting ###
times= []

for rt in risetimes:
    time = datetime.fromtimestamp(rt).strftime("%Y-%m-%dT%H:%M:%S.%f")
    times.append(time)

jprint(times)    