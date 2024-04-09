# Esp32_Cam_Yolov8

In this project, I created a system to control a rover from a distance. It can analyze live video and identify objects. 

The transmitter part has buttons connected to an Arduino, which sends signals to a module called HC-12 for communication.

On the receiver side, another HC-12 module gets signals from the transmitter, controlling the rover's movement through an Arduino.

The rover has a camera (ESP32-CAM) that captures live video. To make the video analysis faster, I added a button that records and processes the video offline.

The system can identify different objects like people, cars, and animals using trained models. I also used a module called HuskyLens to improve object detection accuracy.

Overall, this system lets me control the rover, analyze live video, and identify objects efficiently.

(IMP: Create your own environment and pip install yolov8 and all necessary lib)
