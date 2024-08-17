import cv2
import mediapipe as mp
import time


class hand_detector():
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.maxhands = max_hands
        self.detectioncon = detection_con
        self.trackcon = track_con

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxhands,
                                        min_detection_confidence=self.detectioncon,
                                        min_tracking_confidence=self.trackcon)
        self.mpdraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img
    
    def find_position(self, img, handno=0, draw=True):
        lmlist = []
        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks[handno]
            
            for id, lm in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx , cy =int(lm.x*w), int(lm.y*h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255,0,0), cv2.FILLED)
                    cv2.putText(img, str(id), (cx-5, cy-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
        return lmlist


def main():   
    ptime = 0
    ctime = 0   
    cap = cv2.VideoCapture(0)
    detector = hand_detector()
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
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()