import time

GESTURES = [
    "RED_ON",
    "RED_OFF",
    "YELLOW_ON",
    "YELLOW_OFF",
    "BOTH_ON",
    "BOTH_OFF",
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
