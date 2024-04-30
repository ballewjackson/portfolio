/*
This program reads the joystick X and Y position
and the value of the joystick switch(SW)
and then "pipes" them to serial.

An associated python script can be used to plot 
the data instead of viewing it in Serial monitor.
However, there is a considerable delay in the script.
*/


const int xPin = A0;
const int yPin = A1;
// A pin declared A# is an ananlog pin
// A pin declared # is a digital pin
// so swPin is digital 6
const int swPin = 6;

#define deadzone 20
#define JOY_STICK_OFFSET 512 // this is to set the center position

void setup() {
  Serial.begin(9600); 
  pinMode(swPin, INPUT_PULLUP); // there are several options for pinmode; read the docs for full details https://docs.arduino.cc/learn/microcontrollers/digital-pins
}

void loop() {
  int xPos = analogRead(xPin) - JOY_STICK_OFFSET;
  int yPos = analogRead(yPin) - JOY_STICK_OFFSET;

  if (abs(xPos) <= deadzone) xPos = 0;
  if (abs(yPos) <= deadzone) yPos = 0;

  
  int swState = digitalRead(swPin) == LOW ? 1 : 0; // this inverts the value of swState; there are many other ways to achieve the same result


  // Sending joystick data in the format: x,y,buttonState to serial
  Serial.print(xPos);
  Serial.print(",");
  Serial.print(yPos);
  Serial.print(",");
  Serial.println(swState);

  delay(20);
}
