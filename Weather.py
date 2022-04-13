import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()
OWM_TOKEN = os.getenv("OWM_TOKEN")
#get weather data

def start(location_data, excluded = ""):
    #this returns a lot. so we need to figure out how to parse it further, will do in separate class

    base_url = "https://api.openweathermap.org/data/2.5/onecall"
    one_call = "?lat={}&lon={}&units=imperial&exclude={}&appid={}".format(location_data['latitude'], location_data['longitude'], excluded, OWM_TOKEN)
    url = base_url + one_call

    response = requests.get(url)
    data = json.loads(response.text)

    #print(data)

    return data
