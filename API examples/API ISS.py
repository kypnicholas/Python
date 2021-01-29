import requests
from requests.models import Response
import json

# response = requests.get("http://open-notify.org/Open-Notify-API/People-In-Space/") # simple API to retrieve data about ISS

response = requests.get("https://api.exchangeratesapi.io/latest?symbols=GBP")

print(response.status_code, response.reason)
# print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)    # create a formatted string of the Python JSON object
    print(text)

jprint(response.json())
