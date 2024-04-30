/*
This sketch reads data from a two axis joystick and uses it to control two servos.
These methods could be used for steering or flight controls for a future project.

- Jackson Ballew
*/

#include <Servo.h>

Servo xServo;  // create servo object to control a servo
Servo yServo;

int XjoyPin = A0;  // analog pin used to connect the joystick
int XjoyVal;    // variable to read the value from the analog pin
int YjoyPin = A1;  // analog pin used to connect the joystick
int YjoyVal;    // variable to read the value from the analog pin

void setup() {
  xServo.attach(9);  // attaches the servo on pin 9 to the servo object
  yServo.attach(3);
}

void loop() {
  XjoyVal = analogRead(XjoyPin);            // reads the value of the joystick (value between 0 and 1023)
  XjoyVal = map(XjoyVal, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  xServo.write(XjoyVal);                  // sets the servo position according to the scaled value
  YjoyVal = analogRead(YjoyPin);
  YjoyVal = map(YjoyVal, 0, 1023, 0, 180);
  yServo.write(YjoyVal);
  delay(15);                           // waits for the servo to get there
}
