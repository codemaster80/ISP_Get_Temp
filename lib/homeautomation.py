# This script reads the temperatures from Fritz301 thermostats

import os
from lib import boxlogin
import wget
import json

def loginToFritzBox(user, passwd):
    sid = (boxlogin.get_sid("http://fritz.box", user, passwd))
    print("SID: " + sid)
    return sid


def getTemperatures(acts, sid):
    # requesting temperatures
    temperatures = []
    i = 0
    for el in acts:
        try:
            fritz301 = wget.download("http://fritz.box/webservices/homeautoswitch.lua?ain=" + acts[i] + "&switchcmd=gettemperature&sid=" + sid)
            file = open(fritz301, "r")
            temperatures.append(int(file.read()) / 10)
            file.close()
            os.remove(fritz301)
        except Exception as e:
             print(e)
        i += 1
    return temperatures


def pythonToJSON(obj):
        jsonObj = json.dumps(obj, indent=4)
        return jsonObj
