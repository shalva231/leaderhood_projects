import cv2
import time
import numpy as np
import hand_module as md
import math

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-20.0, None)

volumer = volume.GetVolumeRange()
print(volume.GetVolumeRange())
minvol = volumer[0]
maxvol = volumer[1]





BAR = 400
PERC = 0

cap = cv2.VideoCapture(0)
ptime = 0

detector = md.hand_detector(detection_con=0.7)


while True:
    success, img = cap.read()
    detector.find_hands(img)
    lmlist = detector.find_position(img, draw=False)#we dont want to draw again
    
    
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    
    if len(lmlist) != 0:
        # print(lmlist[4], lmlist[8])
        
        x1 = lmlist[4][1]
        y1 = lmlist[4][2] 
        x2 = lmlist[12][1]
        y2 = lmlist[12][2]
        cy = (y1+y2)//2
        cx = (x1+x2)//2

        cv2.circle(img, (x1, y1), 10, (50, 10, 50), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (50, 10, 50), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (0,0,0), 3)
        cv2.circle(img, (cx, cy), 10, (255,0,255), cv2.FILLED)
        
        cv2.putText(img, str(int(fps)), (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 400), 3)

        lenght = math.hypot(x2-x1,y2-y1) #calculates the lenght (hypothenus)
        if lenght <= 60:
            cv2.circle(img, (cx, cy), 10, (0,255,255), cv2.FILLED)
            
        VOLUME = np.interp(lenght, [50, 300], [minvol, maxvol])
        BAR = np.interp(lenght, [50, 300], [400, 150])
        PERC = np.interp(lenght, [50, 300], [0, 100])
        volume.SetMasterVolumeLevel(VOLUME, None)
        
        
        
    cv2.rectangle(img, (50,150), (85, 400), (0,0,150), 3)    
    cv2.rectangle(img, (50,int(BAR)), (85, 400), (0,255,0), cv2.FILLED)        
    cv2.putText(img, "volume: "+str(int(PERC))+"%", (40,450), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 200, 40),3) 
        
        
    cv2.imshow("shalva", img)
    cv2.waitKey(1)