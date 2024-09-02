import cv2
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()

    cv2.namedWindow("goa the best", cv2.WINDOW_NORMAL) 
    cv2.resizeWindow("goa the best", 100, 50) 
    cv2.imshow("goa the best", img) 
    cv2.waitKey(1) 

print("hello world!")