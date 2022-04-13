from threading import local
import math
import time
##takes weather_data object and custom parameters


## -current, hourly, daily
## -windonly follows and gets only the  wind info

rem_list = ['dt','sunrise','sunset']

def degree_to_direction(deg):
    print("inside directions")
    directions = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    val = int((deg / 22.5) + .5)
    return directions[(val % 16)]

def timestamps_to_msg(obj):
    msg = ""
    msg += "{}\n".format(unix_to_date(obj))
    return msg

def unix_to_date(unix):
    return time.ctime(int(unix))

def start(weather_data,time_select = "",windonly = ""):
    msg = ""
    if time_select == "-current" or len(time_select) == 0:
        #by default or current selected only return current data
        try:
            current_data = weather_data['current']
            #need to convert unix times, and collate a message with the rest of the data
            msg += timestamps_to_msg(current_data['dt'])
            #took out sunrise and sunset
            [current_data.pop(key) for key in rem_list]
            for k,v in current_data.items():
                if k == 'wind_deg':
                    v = degree_to_direction(v)
                msg += "{} : {}\n".format(k, v)

        except Exception as e:
            print(e)
    ##if other modifiers


    return msg





            # msg += "Local Time: {}\n".format(time.ctime(int(current_data['dt'])))
            # msg += "Sunrise: {}\n".format(time.ctime(int(current_data['sunrise'])))
            # msg += "Sunset: {}\n".format(time.ctime(int(current_data['sunset'])))
            # msg += "temp: {}\n".format(current_data['temp'])
            # #optional? 
            # msg += "wind speed: {}\n".format(current_data['wind_speed'])
            # msg += "wind deg: {}\n".format(current_data['wind_deg'])
            # msg += "wind gust: {}\n".format(current_data['wind_gust'])