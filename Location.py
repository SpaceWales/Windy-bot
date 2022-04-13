import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()
PTV_TOKEN = os.getenv("PTV_TOKEN")

#use this to get location

def start(string_location):
    cor = {}

    base_url = "https://api.myptv.com/geocoding/v1/locations/"
    by_text = "by-text?searchText={}&countryFilter=US".format(string_location)
    url = base_url + by_text

    headers = {
        'apiKey': PTV_TOKEN
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    #add city location 
    for a in data['locations']:
        for b in a.values():
            if type(b) is dict:
                if 'latitude' in b:
                    cor = b

    print(cor)
    return cor
    