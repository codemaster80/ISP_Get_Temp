import configparser
from pythonping import ping

def main():
    # reading setup.ini
    parser = configparser.ConfigParser()
    parser.read("config/setup.ini")
    config = parser["config"]

    # initializing variables
    deviceToCheck = config["presencecheck"]

    if(ping(deviceToCheck, timeout=3, count=1, verbose=True)):
        print("online")


if __name__ == "__main__":
    main()
