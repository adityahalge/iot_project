import requests

NODEMCU_IP = "192.168.1.50"
BASE_URL = f"http://{NODEMCU_IP}"

IOT_COMMANDS = {
    "red_on": "/red_on",
    "red_off": "/red_off",
    "yellow_on": "/yellow_on",
    "yellow_off": "/yellow_off",
    "green_on" : "/green_on"
    "green_off" : "/green_off"
    "BOTH_ON": "/both_on",
    "BOTH_OFF": "/both_off",
}

COMMUNICATION = {
    
    "hello": "Hello",
    "yes": "Yes",
    "no": "No",
    "help": "Help",
    "food" : "Food",
    "mission_passed" : "Mission Passed"

}

def send_command(endpoint):
    try:
        requests.get(BASE_URL + endpoint, timeout=2)
    except:
        print("NodeMCU not reachable")

def process_gesture(gesture):
    gesture = gesture.strip().lower()

    if gesture in IOT_COMMANDS:
        send_command(IOT_COMMANDS[gesture])
    elif gesture in COMMUNICATION:
        print(COMMUNICATION[gesture])
    else:
        print("Unknown gesture:", gesture)