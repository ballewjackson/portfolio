/*
This script controls two motors with a amotor control board. 
These methods will be applied for the RC cntrolled rover next.

- Jackson Ballew
*/

// Define the pins
const int ENA = 3; // Enable/speed control pin connected to digital pin 3
const int IN1 = 9; // Connect Motor Direction control pin to digital pin 9
const int IN2 = 8; // Connect Motor Direction control pin to digital pin 8
const int potPin = A0; // Connect Potentiometer to analog pin A0

void setup() {
  // Set the motor control pins as output
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {
  // Read the value from the potentiometer
  int potValue = analogRead(potPin);

  // Map the potentiometer value from (0-1023) to PWM (0-255)
  int motorSpeed = map(potValue, 0, 1023, 0, 255);

  // For one direction, set IN1 HIGH and IN2 LOW
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  // Write the value to the motor speed
  analogWrite(ENA, motorSpeed);
}
