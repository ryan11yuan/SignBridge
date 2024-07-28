import cv2
import mediapipe as mp
import asyncio
import websockets

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# open webcam
cap = cv2.VideoCapture(0)

def detect_hello(landmarks):
    # A very simple "hello" gesture detection based on landmarks
    # Here we'll assume "hello" is when the hand is open (all fingers extended)
    # Customize this logic based on your exact requirements
    fingers = []
    for i in range(4, 21, 4):
        fingers.append(landmarks.landmark[i].y < landmarks.landmark[i - 2].y)
    
    return all(fingers)

def detect_what_is_your_name(landmarks):
    # Simplified gesture detection logic for "What is your name?"
    # Customize this logic based on your exact requirements
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
    ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
    pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x

    # Example condition for "What is your name?" gesture:
    # Let's assume the gesture is recognized when the thumb, index, and middle fingers are touching
    return (abs(thumb_tip - index_tip) < 0.02 and
            abs(index_tip - middle_tip) < 0.02 and
            abs(middle_tip - ring_tip) > 0.1 and
            abs(ring_tip - pinky_tip) > 0.1)

async def detect_jump(websocket, path):
    
    while True:

        # read frame from webcam
        ret, frame = cap.read()

        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        # Draw hand landmarks
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if detect_hello(hand_landmarks):
                    print("Hello")
                    await websocket.send("Hello")
                elif detect_what_is_your_name(hand_landmarks):
                    print("What is your name?")
                    await websocket.send("What is your name?")

        await asyncio.sleep(0.01)

    cap.release()

async def main():
    async with websockets.serve(detect_jump, "localhost", 8766):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())