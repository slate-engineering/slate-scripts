import requests
import json as JSON

url = "https://slate.host/api/v1/get-slate"
headers = {
    "content-type": "application/json",
    "Authorization": "Basic SLA8d5a9c28-cb14-4886-b4ac-5575da2d90aaTE",
}
json = {"id": "8eb2d471-9abf-4eae-a461-c62ebeb529b0"}

r = requests.post(url, headers=headers, json=json)

print(JSON.dumps(r.json(), indent=2, sort_keys=True))
