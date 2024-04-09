import cv2
from ultralytics import YOLO

url = 'http://192.168.4.1:81/stream'
#model
# Create a VideoCapture object
cap = cv2.VideoCapture(url)
model = YOLO("yolov8n.pt", "v8") 

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

frame_skip = 1  # Adjust this value to skip frames (e.g., 1 for no skip, 2 for every 2nd frame, etc.)
frame_width = 640  # Adjust this value for the desired width of frames

# Read and display frames from the camera
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Resize the frame to reduce processing load
        frame = cv2.resize(frame, (frame_width, int(frame.shape[0] * frame_width / frame.shape[1])))

        # Skip frames if needed
        if frame_skip > 1:
            for _ in range(frame_skip - 1):
                _, _ = cap.read()

        # Perform object detection using YOLOv8
        result = model.predict(source=frame, show=True)
        print(result)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
