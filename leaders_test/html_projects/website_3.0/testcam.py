import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    success, img = cap.read()
    
    if not success:
        print("Error: Could not read frame.")
        break

    cv2.namedWindow("goa the best", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("goa the best", 135, 110)
    cv2.imshow("goa the best", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

