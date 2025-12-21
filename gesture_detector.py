import time

GESTURES = [
    "LIGHT_ON",
    "LIGHT_OFF",
    "FAN_ON",
    "FAN_OFF",
    "DEVICE3_ON",
    "DEVICE3_OFF",
    "HELLO",
    "YES",
    "NO",
    "THANK_YOU",
    "HELP",
    "CUSTOM_ACTION"
]

index = 0

def detect_gesture():
    global index
    time.sleep(2)
    gesture = GESTURES[index]
    index = (index + 1) % len(GESTURES)
    return gesture
