import cv2
import mediapipe as mp
import time
import hand_module as mod



ptime = 0
ctime = 0   
cap = cv2.VideoCapture(0)
detector = mod.hand_detector()
while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lmlist = detector.find_position(img)
    if len(lmlist) != 0:
        print(lmlist[0])        
        
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 3)

    cv2.imshow("goa the best", img)
    cv2.waitKey(1)