import random
import cv2
from ultralytics import YOLO

# Open the class list file and read the classes
with open("utils/coco.txt", "r") as file:
    class_list = file.read().split("\n")

# Generate random colors for class list
detection_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    for _ in range(len(class_list))]

# Load the YOLOv8n model
model = YOLO("weights/yolov8n.pt", "v8")

# Open the video file for processing
cap = cv2.VideoCapture("recording_2024-04-06_14-29-12.avi")

if not cap.isOpened():
    print("Cannot open video file")
    exit()

# Get the video frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for saving the video
out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Predict on image
    detect_params = model.predict(source=[frame], conf=0.45, save=False)

    if len(detect_params[0]) != 0:
        for i, box in enumerate(detect_params[0].boxes):
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]

            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsID)],
                3,
            )

            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )

    # Write the frame with annotations to the output video
    out.write(frame)

    # Display the resulting frame
    cv2.imshow("ObjectDetection", frame)

    # Terminate run when "Q" pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()
