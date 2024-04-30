/*
This is the control script for my radio controlled rover.
The rover uses a small onboard radio to recieve controls and it can drive around.

- Jackson Ballew
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>


RF24 radio(2,3); // CE, CSN

const byte address[6] = "00001";

struct point {
    int x;
    int y;
};

class Receiver {
  RF24& radio; // Reference to RF24 object

public:
  Receiver(RF24& radioRef) : radio(radioRef) {} // Constructor

  void setup(const byte address[6]) {
    radio.begin();
    radio.openReadingPipe(1, address);
    radio.setPALevel(RF24_PA_MIN);
    radio.startListening();
    if (radio.isChipConnected()){
      Serial.println("RF24 module connected.");
    }
    else {
      Serial.println("RF24 module not found.");
    }
  }

  point read() {
    point data;
    if (radio.available()){
      radio.read(&data, sizeof(data));
      Serial.println("Receivied data.");
      Serial.print(data.x);
      Serial.print(",");
      Serial.println(data.y);
    } else {
      data.y = 0;
      data.x = 0;
    }
    return data;
  }

};

Receiver receiver(radio); 

#include <Arduino.h>

//#define deadzone 50
// absolute max is 255
#define maxMotor 210

struct Motor {
  // should be 0 - maxMotor
  int motorspeed;
  const int controlPin;
  const int directionPin1;
  const int directionPin2;

  Motor(int controlPin, int directionPin1, int directionPin2) : 
  motorspeed(0), controlPin(controlPin), 
  directionPin1(directionPin1), directionPin2(directionPin2)
  {
    pinMode(controlPin, OUTPUT);
    pinMode(directionPin1, OUTPUT);
    pinMode(directionPin2, OUTPUT);
  }

  void setForward() {
    digitalWrite(directionPin1, HIGH);
    digitalWrite(directionPin2, LOW);
  }

  void setReverse() {
    digitalWrite(directionPin1, LOW);
    digitalWrite(directionPin2, HIGH);
  }

  void stop() {digitalWrite(controlPin, LOW);}

  void setSpeed(int speed) {
    // speed should be 0 - maxMotor
    analogWrite(controlPin, speed); 
  }
};


/*
#define JOY_STICK_OFFSET 512
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
};*/

double mapDouble(double x, double in_min, double in_max, double out_min, double out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

class Platform {
  private:
      Motor& leftMotor;
      Motor& rightMotor;
      //JoyStick& js;
      Receiver& receiver;
      
      void moveForward(int speed) {
          leftMotor.setForward();
          rightMotor.setForward();
          leftMotor.setSpeed(speed);
          rightMotor.setSpeed(speed);
      }

      void moveBackward(int speed) {
          leftMotor.setReverse();
          rightMotor.setReverse();
          leftMotor.setSpeed(speed);
          rightMotor.setSpeed(speed);
      }

      void turnLeft(int speed) {
          leftMotor.setReverse();
          rightMotor.setForward();
          leftMotor.setSpeed(speed);
          rightMotor.setSpeed(speed);
      }

      void turnRight(int speed) {
          leftMotor.setForward();
          rightMotor.setReverse();
          leftMotor.setSpeed(speed);
          rightMotor.setSpeed(speed);
      }

  public:
      /*Platform(Motor& leftMotor, Motor& rightMotor, JoyStick& js) 
          : leftMotor(leftMotor), rightMotor(rightMotor), js(js) 
      {}*/
      Platform(Motor& leftMotor, Motor& rightMotor, Receiver& receiver) 
          : leftMotor(leftMotor), rightMotor(rightMotor), receiver(receiver) 
      {}

      void update() {
        point data = receiver.read();
        int baseSpeed;
        
        if (data.y == 0 && data.x == 0) {
            leftMotor.stop();
            rightMotor.stop();
        } else if (abs(data.y) > abs(data.x)) {
            baseSpeed = map(abs(data.y), 0, 512, 0, maxMotor);
            if (data.y < 0) moveForward(baseSpeed);
            else moveBackward(baseSpeed);
        } else {
            baseSpeed = map(abs(data.x), 0, 512, 0, maxMotor);
            if (data.x < 0) turnLeft(baseSpeed);
            else turnRight(baseSpeed);
        }
      }
};



Motor leftMotor(10, 8, 7);
Motor rightMotor(9, 6, 5);
//JoyStick js(A1, A2);

//Platform platform(leftMotor, rightMotor, js);
Platform platform(leftMotor, rightMotor, receiver);

void setup(void){
  Serial.begin(9600);
  receiver.setup(address);
}

void loop(void){
  platform.update();
  delay(50);
}




