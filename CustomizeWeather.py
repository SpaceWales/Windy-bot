from threading import local
import math
import time
##takes weather_data object and custom parameters


## -current, hourly, daily
## -windonly follows and gets only the  wind info

rem_list = ['dt','temp','wind_deg','wind_speed','wind_gust','weather']
keep_list = ['dt','wind_deg','wind_speed','wind_gust']
weather_rem = ['description']

def degree_to_direction(deg):
    directions = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    val = int((deg / 22.5) + .5)
    return directions[(val % 16)]

def timestamps_to_msg(obj):
    return "{}\n".format(unix_to_date(obj))

def unix_to_date(unix):
    return time.ctime(int(unix))

def clean_weather_obj(arr):
    #only 1, I know this is ugly
    for obj in arr:
        newdict = {k: obj[k] for k in weather_rem}
        obj = newdict
    return obj

def assemble_message_with_selection(current_data, windonly):
    msg = ""
    
    if windonly:
        newdict = {k: current_data[k] for k in keep_list}
        current_data = newdict
    else:
        newdict = {k: current_data[k] for k in rem_list}
        current_data = newdict

    msg += timestamps_to_msg(current_data['dt'])
    current_data.pop('dt')

    #get rid of weather data
    if not windonly:
        current_data['weather'] = clean_weather_obj(current_data['weather'])

    for k,v in current_data.items():
        if k == 'wind_deg':
            v = degree_to_direction(v)
        msg += "{} : {}\n".format(k, v)
    
    return msg

def start(current_data, windonly = True):
    msg = ""
    try:
        msg = assemble_message_with_selection(current_data, windonly)
    except Exception as e:
        print(e)
    return msg