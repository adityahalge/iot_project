import requests

NODEMCU_IP = "192.168.1.50"
BASE_URL = f"http://{NODEMCU_IP}"

IOT_COMMANDS = {
    "LIGHT_ON": "/light_on",
    "LIGHT_OFF": "/light_off",
    "FAN_ON": "/fan_on",
    "FAN_OFF": "/fan_off",
    "DEVICE3_ON": "/device3_on",
    "DEVICE3_OFF": "/device3_off",
}

COMMUNICATION = {
    "HELLO",
    "YES",
    "NO",
    "THANK_YOU",
    "HELP"
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
