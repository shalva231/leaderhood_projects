import cv2
import mediapipe as mp
import time


# getting my vebcams campure
cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpdraw = mp.solutions.drawing_utils


#write fps
#previouse time
ptime = 0
#curent time
ctime = 0




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
    # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        #we will extract information of each hand with this for loop
        for handLms in result.multi_hand_landmarks:
            #get index of the dots and the landmark(x y z cordinates)
            for id, lm in enumerate(handLms.landmark):
                #we can check the id and lm by printing them
                #lm doesnt give us pixels we can multiply the value it gives by width and height and then we will know the pixel value
                # print(id,lm)
                
                # find width height 
                h, w, c = img.shape
                cx , cy =int(lm.x*w), int(lm.y*h)
                #print id of the point and the x y cordinates
                # print(id, cx, cy)
                
                # just makes a circle on the botom dot
                # we can remove if statement here to draw on all the dots
                # if id == 0:
                #   cv2.circle(img, (cx, cy), 25, (255, 50, 255), cv2.FILLED)
                
                #put the id and the x y cordinates in a lst
                
            
            
            #single hand| handlms draws dots| the last one draws connections
            mpdraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) 
             
            
        
    #calculate fps
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    
    #display fps
    #                               position        font            size  color  thicness
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 3)
    
    #running webcam    
    cv2.imshow("goa the best", img)
    cv2.waitKey(1)