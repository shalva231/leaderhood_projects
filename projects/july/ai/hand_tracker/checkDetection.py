import cv2
import mediapipe as mp
import time


#running webcam 
cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    
    success, img = cap.read()
    #convert to rgb
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #process the frame and gives the result
    result = hands.process(imgRGB)
    
    
    
    #extract information from result
    
    
    
    #print result
    # print(result)
    #check if somthing is detected
    print(result.multi_hand_landmarks)
        
        
    #running webcam    
    cv2.imshow("goa the best", img)
    cv2.waitKey(1)