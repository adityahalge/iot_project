from gesture_detector import detect_gesture
from command_mapper import process_gesture

print("=== Gesture Controlled IoT System ===")

while True:
    gesture = detect_gesture()
    print(f"\nDetected Gesture: {gesture}")
    process_gesture(gesture)
