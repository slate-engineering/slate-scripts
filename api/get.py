import requests
import json as JSON

url = "https://slate.host/api/v1/get"
headers = {
    "content-type": "application/json",
    "Authorization": "SLA8d5a9c28-cb14-4886-b4ac-5575da2d90aaTE",
}

json = {"private": "true"}

get = requests.post(url, headers=headers, json=json)

print(JSON.dumps(get.json(), indent=2))
