import requests
from requests.models import Response
import json

response = requests.get("https://jobs.github.com/positions.json?description=python&location=frankfurt")


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())




