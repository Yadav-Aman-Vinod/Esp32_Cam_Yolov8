#include <SoftwareSerial.h>
#include <AFMotor.h> // Include the Adafruit Motor Shield library

SoftwareSerial hc12(A0, A1); // HC-12 TX Pin, HC-12 RX Pin

AF_DCMotor motor1(1); // Motor 1 is connected to M1 port of the motor shield
AF_DCMotor motor2(2); // Motor 2 is connected to M2 port of the motor shield
AF_DCMotor motor3(3); // Motor 3 is connected to M3 port of the motor shield
AF_DCMotor motor4(4); // Motor 4 is connected to M4 port of the motor shield

const int left = 1;
const int right = 4;
const int forward = 2;
const int backward = 3;

const int Speed = 200; // Maximum motor speed
const int maxSpeed = 255; // Maximum motor speed

unsigned long lastSignalTime = 0; // Timestamp of last received signal
const unsigned long signalTimeout = 100; // Signal timeout in milliseconds

void setup() {
  Serial.begin(9600); // Initialize serial communication for debugging
  hc12.begin(9600); // Set baud rate to match HC-12 module
  
  // Set initial motor speed
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  motor3.setSpeed(0);
  motor4.setSpeed(0);
  
  // Start motor
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void loop() {
  // Check for HC-12 data
  while (hc12.available() > 0) {
    // Read data from HC-12
    String data = hc12.readStringUntil('\n');

    // Update last signal time
    lastSignalTime = millis();

    // Print received data for debugging
    Serial.println(data);

    // Process button data and control motors
    processButtonData(data);
  }

  // Check if signal timeout has occurred
  if (millis() - lastSignalTime > signalTimeout) {
    motorStop(); // Stop motors if no signal received for timeout period
  }
}

// Process button data and control motors
void processButtonData(String data) {
  int button = data.toInt();

  // Print button value for debugging
  Serial.print("Button: ");
  Serial.println(button);

  if (button == forward) {
    motorForward();
  } else if (button == backward) {
    motorBackward();
  } else if (button == left) {
    motorLeft();
  } else if (button == right) {
    motorRight();
  } else {
    motorStop(); // Stop motors for invalid or no button press
  }
}

// Motor control functions
void motorStop() {
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  motor3.setSpeed(0);
  motor4.setSpeed(0);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void motorLeft() {
  motor1.setSpeed(maxSpeed);
  motor2.setSpeed(maxSpeed);
  motor3.setSpeed(maxSpeed);
  motor4.setSpeed(maxSpeed);
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

void motorRight() {
  motor1.setSpeed(maxSpeed);
  motor2.setSpeed(maxSpeed);
  motor3.setSpeed(maxSpeed);
  motor4.setSpeed(maxSpeed);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

void motorBackward() {
  motor1.setSpeed(Speed);
  motor2.setSpeed(Speed);
  motor3.setSpeed(Speed);
  motor4.setSpeed(Speed);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

void motorForward() {
  motor1.setSpeed(Speed);
  motor2.setSpeed(Speed);
  motor3.setSpeed(Speed);
  motor4.setSpeed(Speed);
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}
