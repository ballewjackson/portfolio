/*
This is the script for the 1 joystick controller for the RC rover.

- Jackson Ballew
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define deadzone 15
#define JOY_STICK_OFFSET 512

RF24 radio(7,8); // CE, CSN

const byte address[6] = "00001";

struct JoyStick {
  int xPin;
  int yPin;
  JoyStick(int xPin, int yPin) : xPin(xPin), yPin(yPin) {}
  int xPos;
  int yPos;
  void readPosition() {
    xPos = analogRead(xPin) - JOY_STICK_OFFSET;
    yPos = analogRead(yPin) - JOY_STICK_OFFSET;
    
    if (abs(xPos) <= deadzone) xPos = 0;
    if (abs(yPos) <= deadzone) yPos = 0;
  }
};

struct point {
    int x;
    int y;
};

class Transmitter {
  RF24& radio; // Reference to RF24 object

public:
  Transmitter(RF24& radioRef) : radio(radioRef) {} // Constructor

  void setup(const byte address[6]) {
    radio.begin();
    radio.openWritingPipe(address);
    radio.setPALevel(RF24_PA_MIN);
    radio.stopListening();
    if (radio.isChipConnected()){
      Serial.println("RF24 module connected.");
    }
    else {
      Serial.println("RF24 module not found.");
    }
  }

  void send(const point& p) {
    //radio.write(&p, sizeof(p));
    if (radio.write(&p, sizeof(p))) {
      Serial.println("Data sent successfully");
    } else {
      Serial.println("Failed to send data");
    }

  }
};

Transmitter transmitter(radio);

void setup() {
  Serial.begin(9600);
  transmitter.setup(address);
}

void loop() {
  JoyStick joystick(A0, A1); // define the pins you're using for your joystick
  joystick.readPosition();
  
  point p;
  p.x = joystick.xPos;
  p.y = joystick.yPos;
  
  transmitter.send(p);
  delay(20);
}
