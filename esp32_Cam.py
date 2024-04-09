import cv2

url = 'http://192.168.4.1:81/stream'

# Create a VideoCapture object
cap = cv2.VideoCapture(url)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

# Read and display frames from the camera
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('ESP32-CAM Stream', frame)
        # Press 'q' to exitq
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
