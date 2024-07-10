import cv2
import mediapipe as mp
import time

mppose = mp.solutions.pose
pose = mppose.Pose()


mpdraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

ptime = 0


while True:

    success, img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgrgb)
    if results.pose_landmarks:
        mpdraw.draw_landmarks(img, results.pose_landmarks, mppose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            cv2.putText(img, str(id), (cx-5, cy-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
            
            
        
        
    ctime = time.time()
    fps = 1/(ctime-ptime) 
    ptime = ctime
    
    
    cv2.putText(img, "goaTheBest", (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (155,0,0),3)   
    cv2.imshow("!!!!!!goa the best!!!!!!", img)
    cv2.waitKey(1)