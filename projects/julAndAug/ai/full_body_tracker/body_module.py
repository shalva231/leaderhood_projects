import cv2
import mediapipe as mp
import time

class pose_detector():
    def __init__(self, mode=False, upper=False, smoothness=True, detc=0.5, trackc=0.5):
        self.mode = mode
        self.upper = upper
        self.smoothness = smoothness
        self.detc = detc
        self.trackc = trackc
        
        self.mppose = mp.solutions.pose
        self.pose = self.mppose.Pose(
            static_image_mode=self.mode,
            model_complexity=1,
            smooth_landmarks=self.smoothness,
            enable_segmentation=False,
            min_detection_confidence=self.detc,
            min_tracking_confidence=self.trackc
        )
        self.mpdraw = mp.solutions.drawing_utils
        self.results = None

    def findpose(self, img, draw=True):
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgrgb)
       
        if self.results.pose_landmarks: 
            if draw:
                self.mpdraw.draw_landmarks(img, self.results.pose_landmarks, self.mppose.POSE_CONNECTIONS)
        
        return img
    
    def getpose(self, img, draw=True):
        lmlist = []
        if self.results and self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
                    cv2.putText(img, str(id), (cx-5, cy-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
        return lmlist

def main():
    cap = cv2.VideoCapture("1.mp4")
    ptime = 0
    detector = pose_detector()
    
    while True:
        success, img = cap.read()
        img = detector.findpose(img)
        lmlist = detector.getpose(img)
        if len(lmlist) != 0:
            print(lmlist)
        
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (155, 0, 0), 3)
        cv2.imshow("!!!!!!goa the best!!!!!!", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
