from ultralytics import YOLO
import numpy
import cv2

model = YOLO("yolov8n.pt", "v8")  

result = model.predict(source="0",show = True)

print(result)