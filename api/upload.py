import requests

url = "https://uploads.slate.host/api/public/8eb2d471-9abf-4eae-a461-c62ebeb529b0"
files = {"file": open("example-file.txt", "rb")}
headers = {"Authorization": "Basic SLA8d5a9c28-cb14-4886-b4ac-5575da2d90aaTE"}

r = requests.post(url, headers=headers, files=files)
