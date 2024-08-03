import cv2
import mediapipe as mp
import time
import body_module as md



cap = cv2.VideoCapture(0)
ptime = 0
detector = md.pose_detector()
    
while True:
    success, img = cap.read()
    img = detector.findpose(img)
    lmlist = detector.getpose(img)
    if len(lmlist) != 0:
        print(lmlist[0],lmlist[2],lmlist[4],lmlist[6],lmlist[8])
        
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (155, 0, 0), 3)
    cv2.imshow("!!!!!!goa the best!!!!!!", img)
    cv2.waitKey(1)