# You need to install requests for this to work.
import requests

API_BASE_URL = "http://127.0.0.1:8000"

# Use the following when uploading to TAPAS, not the local development site
# API_BASE_URL = "https://starserver.thelangton.org.uk/tapas"

headers = {
    'Authorization': 'Token 6ee8ac72a45d5f9cebd9e1ffacaf6df85f2c2449',  # You MUST include the 'Token' part here before the API token
}


# The / at the end of upload is VERY important here! You'll get an Internal Server Error without it.
# .... I speak from experience
r = requests.get(API_BASE_URL + "/api/v1/project/", headers=headers)

print(r.json())
