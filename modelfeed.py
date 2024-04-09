import cv2
from datetime import datetime

url = 'http://192.168.4.1:81/stream'
#model
# Create a VideoCapture object
cap = cv2.VideoCapture(url)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

# Initialize recording flag and video writer
is_recording = False
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for saving the video
out = None

# Read and display frames from the camera
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('ESP32-CAM Stream', frame)

        # Check for keypress events
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):  # Exit if 'q' is pressed
            break
        elif key & 0xFF == ord('r'):  # Start/stop recording if 'r' is pressed
            if not is_recording:
                # Start recording
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"recording_{timestamp}.avi"
                out = cv2.VideoWriter(filename, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
                is_recording = True
                print("Recording started.")
            else:
                # Stop recording
                out.release()
                is_recording = False
                print("Recording stopped. Video saved as:", filename)

        # Write frame to video file if recording
        if is_recording:
            out.write(frame)
    else:
        break

# Release the VideoCapture object, writer, and close all windows
cap.release()
cv2.destroyAllWindows()
