# this script reads data from fritz 301 heating controls and send the data to a mqtt broker

import configparser
from lib import homeautomation as fha
import paho.mqtt.publish as mqtt

def main():
    # reading setup.ini
    parser = configparser.ConfigParser()
    parser.read("setup.ini")
    config = parser["config"]

    # initializing variables
    username = config["username"]
    password = config["password"]
    actuators = [
        config["actuator1"], config["actuator2"], config["actuator3"],
        config["actuator4"], config["actuator5"]
    ]

    # Login to FritzBox to request a SID
    sid = fha.loginToFritzBox(username, password)
    # get room temperatures measured by thermostats
    temperatures = fha.getTemperatures(actuators, sid)


    # sending temperatures to mqtt broker
    print("Roomtemperatures: ", temperatures)
    mqtt.single(topic="/heizungsthermostate/raumtemperatur/arbeitszimmer", payload=temperatures[0], port=1883,
                hostname="raspberrypi")
    mqtt.single(topic="/heizungsthermostate/raumtemperatur/badezimmer", payload=temperatures[1], port=1883,
                hostname="raspberrypi")
    mqtt.single(topic="/heizungsthermostate/raumtemperatur/schlafzimmer", payload=temperatures[2], port=1883,
                hostname="raspberrypi")
    mqtt.single(topic="/heizungsthermostate/raumtemperatur/wohnzimmer", payload=temperatures[3], port=1883,
                hostname="raspberrypi")
    mqtt.single(topic="/heizungsthermostate/raumtemperatur/kueche", payload=temperatures[4], port=1883,
                hostname="raspberrypi")

    # converting to JSON-file for AJAX use
    # roomTemperatures = {
    #                     "workspace": temperatures[0],
    #                     "bath": temperatures[1],
    #                     "bedroom": temperatures[2],
    #                     "livingroom": temperatures[3],
    #                     "kitchen": temperatures[4]
    #                     }
    # if os.path.exists("temperatures.json"):
    #     os.remove("temperatures.json")
    #
    # jsonFile = open("temperatures.json", "x")
    # jsonFile.write(fha.pythonToJSON(roomTemperatures))
    # jsonFile.close()


if __name__ == "__main__":
    main()
