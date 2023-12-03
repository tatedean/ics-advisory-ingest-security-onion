import requests
import os, sys
import requests

headers = {
    "X-RapidAPI-Key": os.environ.get("ADVISORY_API_KEY"),
    "X-RapidAPI-Host": "ics-ap-apis.p.rapidapi.com"
}

urls = {
    "latest": "https://ics-ap-apis.p.rapidapi.com/advisory/latest",
    "advisoryById": "https://ics-ap-apis.p.rapidapi.com/advisory/id",
}

def putMappings(config, mappings):
    xheaders = {
        "Content-Type" : "application/json",
    }
    url = config.get('ES_HOST') + ':' + config.get('ES_PORT') + "/icsadvisory"
    response = requests.put(url, headers=xheaders, json=mappings)
    print(response)

def getLatestAdvisories(n=3):
    url = urls["latest"]
    querystring = {"n":n}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        # Assuming the API returns JSON data
        if response.status_code == 200:
            return(response.status_code, response.json())
        else:
            return(response.status_code, {})
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def getAdvisoryById(advId):
    url = urls["advisoryById"]
    querystring = {"advisoryId":advId}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        # Assuming the API returns JSON data
        if response.status_code == 200:
            return(response.status_code, response.json())
        else:
            return(response.status_code, {})
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def testRapidAPI():
    url = urls["latest"]
    querystring = {"n":"3"}
    response = requests.get(url, headers=headers, params=querystring)

    return(response.json())