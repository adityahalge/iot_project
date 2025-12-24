import requests

NODEMCU_IP = "192.168.1.50"
BASE_URL = f"http://{NODEMCU_IP}"

IOT_COMMANDS = {
    "RED_ON": "/red_on",
    "RED_OFF": "/red_off",
    "YELLOW_ON": "/yellow_on",
    "YELLOW_OFF": "/yellow_off",
    "BOTH_ON": "/both_on",
    "BOTH_OFF": "/both_off",
}

COMMUNICATION = {
    
    "HELLO": "Hello",
    "YES": "Yes",
    "NO": "No",
    "THANK_YOU": "Thank you",
    "HELP": "Help"


}

def send_command(endpoint):
    print(f"[IoT] Sending request to {BASE_URL}{endpoint}")
    # requests.get(BASE_URL + endpoint)

def process_gesture(gesture):
    if gesture in IOT_COMMANDS:
        send_command(IOT_COMMANDS[gesture])
    elif gesture in COMMUNICATION:
        print(f"[COMMUNICATION] {gesture}")
    elif gesture == "CUSTOM_ACTION":
        print("[CUSTOM] Custom gesture detected")
    else:
        print("[UNKNOWN] Gesture")
