import cv2

def test_camera(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"Error: Could not open camera {index}")
        return
    
    print(f"Displaying camera {index}... Press 'q' to quit.")

    while True:
        success, img = cap.read()
        if not success:
            print(f"Error: Could not read frame from camera {index}.")
            break

        cv2.imshow(f"Camera {index}", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Test all cameras
for i in range(3):
    print(f"Testing camera {i}...")
    test_camera(i)

