import requests
import os
import requests

url = "https://ics-ap-apis.p.rapidapi.com/advisory/latest"

querystring = {"n":"3"}

headers = {
    "X-RapidAPI-Key": os.environ.get("ADVISORY_API_KEY"),
    "X-RapidAPI-Host": "ics-ap-apis.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())