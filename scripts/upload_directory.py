import os
import requests
from requests_toolbelt import MultipartEncoder

url = "https://uploads.slate.host/api/public/8eb2d471-9abf-4eae-a461-c62ebeb529b0"
# API key of dev-examples slate-managed account, password on notion
headers = {"Authorization": "Basic SLA6f6a789f-0031-4098-b037-c3d9f6e514c0TE"}

# get dir to upload from
direc = "/Users/toast/my-docs/bookz"

# array of files in direc
upload_files = [i for i in os.listdir(direc)]
files_field = {}

# iterate over files in directory, stream upload to slate
for f in upload_files:
    file_path = os.path.join(direc, f)
    if f != ".DS_Store":
        m = MultipartEncoder(fields={"file": (f, open(file_path, "rb"))})
        headers["Content-Type"] = m.content_type
        r = requests.post(url, data=m, headers=headers)
        print(r.status_code)

