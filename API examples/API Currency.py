import requests
from requests.models import Response
import json

response = requests.get("https://api.exchangeratesapi.io/latest?symbols=GBP")

### (1) Inline printing ###
text = json.dumps(response.json(), sort_keys=True, indent=4)
print("Test 1 - inline")
print(text)

### (2) create function that serializes and prints any given (obj) ###
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)    # create a formatted string of the Python JSON object
    print(text)

print("Test 2 - via method")
jprint(response.json())