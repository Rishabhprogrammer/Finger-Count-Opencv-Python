import HandDectector
import cv2
import math
import numpy as np

def fingercounter():
        
    handDetector = HandDectector(min_detection_confidence=0.7)
    webcamFeed = cv2.VideoCapture(0)

    while True:
        status, image = webcamFeed.read()
        handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
        count=0

        if(len(handLandmarks) != 0):
            #we will get y coordinate of finger-tip and check if it lies above middle landmark of that finger
            #details: https://google.github.io/mediapipe/solutions/hands

            if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:       #Right Thumb
                count = count+1
                #Speak(count)
            elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:       #Left Thumb
                count = count+1
                #Speak(count)
            if handLandmarks[8][2] < handLandmarks[6][2]:       #Index finger
                count = count+1
                #Speak(count)
            if handLandmarks[12][2] < handLandmarks[10][2]:     #Middle finger
                count = count+1
                #Speak(count)
            if handLandmarks[16][2] < handLandmarks[14][2]:     #Ring finger
                count = count+1
                #Speak(count)
            if handLandmarks[20][2] < handLandmarks[18][2]:     #Little finger
                count = count+1
                #Speak(count)

        cv2.putText(image, str(count), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)
        cv2.imshow("Finger Count", image)
        
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break
        
    webcamFeed.release()

fingercounter()