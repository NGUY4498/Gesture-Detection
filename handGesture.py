import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,600)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,500)

mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

def findGesture(hand):
    if hand.landmark[8].y > hand.landmark[6].y:
        navigate("fist")
    elif hand.landmark[8].y < hand.landmark[6].y:
        navigate("flex")

def navigate(gesture):
    match gesture:
        case "fist":
            #replace prints to pyautogui to move mouse
            print("fist")
        case "flex":
            print("flex")

while True:
    success, frame = cam.read()
    if success:
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result = hand.process(image)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                findGesture(hand_landmarks)
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()