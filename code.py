import cv2 
import mediapipe as mp
camara=cv2.VideoCapture(0)
mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
hands=mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)
tipid=[4,8,12,16,20]
def drawlandmark(image,hand_landmark):
    if hand_landmark:
        for l in hand_landmark:
            mp_drawing.draw_landmarks(image,l,mp_hands.HAND_CONNECTIONS)

while True:
    succes,image=camara.read()
    image=cv2.flip(image,1)
    results=hands.process(image)
    hand_landmark=results.multi_hand_landmarks
    drawlandmark(image,hand_landmark)
    cv2.imshow('output',image)
    if cv2.waitKey(1)==32:
        break