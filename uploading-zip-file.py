# You need to install requests for this to work.
import requests

API_BASE_URL = "http://127.0.0.1:8000"

file_path = "demo.zip"  # The path to the ZIP file you want to upload. Make sure it exists!

# Use the following when uploading to TAPAS, not the local development site
# API_BASE_URL = "https://starserver.thelangton.org.uk/tapas"

headers = {
    'Authorization': 'Token 6ee8ac72a45d5f9cebd9e1ffacaf6df85f2c2449',  # You MUST include the 'Token' part here before the API token
}

payload = {
    'name': 'Name of Upload',  # Name of the upload, can be whatever you like, but make it meaningful
    'project': '1',  # You MUST specify a project in ID form here!
                     # You can check all project IDs via the API too :)
    'latitude': '1',  # Latitude of where data was taken, needed if you choose RAY as a project
    'longitude': '1',  # Longitude of where data was taken, needed if you choose RAY as a project
}

# The / at the end of upload is VERY important here! You'll get an Internal Server Error without it.
# .... I speak from experience
r = requests.post(API_BASE_URL + "/api/v1/upload/", files={"zipfile": open(file_path, 'rb')}, data=payload, headers=headers)

print(r.text)
