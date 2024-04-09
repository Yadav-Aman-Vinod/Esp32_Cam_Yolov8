#include <SoftwareSerial.h>

SoftwareSerial hc12(2, 3); // HC-12 TX Pin, HC-12 RX Pin
const int button1Pin = 4; // Pin for button 1
const int button2Pin = 5; // Pin for button 2
const int button3Pin = 6; // Pin for button 3
const int button4Pin = 7; // Pin for button 4

void setup() {
  Serial.begin(9600); // Initialize serial communication for debugging
  hc12.begin(9600); // Set baud rate to match HC-12 module
  pinMode(button1Pin, INPUT); // Set button pins as input with internal pull-up resistors
  pinMode(button2Pin, INPUT);
  pinMode(button3Pin, INPUT);
  pinMode(button4Pin, INPUT);
}

void loop() {
  // Read button states
  int button1State = digitalRead(button1Pin);
  int button2State = digitalRead(button2Pin);
  int button3State = digitalRead(button3Pin);
  int button4State = digitalRead(button4Pin);




  // Check if any button is pressed and send the corresponding button number
  if (button1State == 0) {
    hc12.println("1");
  } else if (button2State == 0) {
    hc12.println("2");
  } else if (button3State == 0) {
    hc12.println("3");
  } else if (button4State == 0) {
    hc12.println("4");
  }

  delay(100); // Adjust delay as needed to control transmission frequency
}
