import requests
import json as JSON

headers = {
    "content-type": "application/json",
    "Authorization": "Basic SLA8d5a9c28-cb14-4886-b4ac-5575da2d90aaTE",
}
json = {"id": "8eb2d471-9abf-4eae-a461-c62ebeb529b0"}
get_slate = requests.post(
    "https://slate.host/api/v1/get-slate", headers=headers, json=json
)

get_slate_response = get_slate.json()

slate = get_slate_response["slate"]
# change a field in the slate response
slate["data"]["objects"][0]["title"] = "i changed the title"

url = "https://slate.host/api/v1/update-slate"
updated_data = {"data": slate}

update_slate = requests.post(url, headers=headers, json=updated_data)
