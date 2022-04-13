from threading import local
import time
##takes weather_data object and custom parameters


## -current, hourly, daily
## -windonly follows and gets only the  wind info

def start(weather_data,time_select = "",windonly = ""):
    msg = ""
    if time_select == "-current" or len(time_select) == 0:
        #by default or current selected only return current data
        current_data = weather_data['current']
        msg += "Local Time: {}\n".format(time.ctime(int(current_data['dt'])))
        msg += "Sunrise: {}\n".format(time.ctime(int(current_data['sunrise'])))
        msg += "Sunset: {}\n".format(time.ctime(int(current_data['sunset'])))
        msg += "temp: {}\n".format(current_data['temp'])
        #optional? 
        msg += "wind speed: {}\n".format(current_data['wind_speed'])
        msg += "wind deg: {}\n".format(current_data['wind_deg'])
        msg += "wind gust: {}\n".format(current_data['wind_gust'])
    ##if other modifiers
    return msg
