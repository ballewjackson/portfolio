/*
First dablings in using OOP for the motor and joystick for the RC rover project.

- Jackson Ballew
*/

#include <Arduino.h>

#define deadzone 50
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
};

double mapDouble(double x, double in_min, double in_max, double out_min, double out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

class Platform {
  private:
      Motor& leftMotor;
      Motor& rightMotor;
      JoyStick& js;
      
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
      Platform(Motor& leftMotor, Motor& rightMotor, JoyStick& js) 
          : leftMotor(leftMotor), rightMotor(rightMotor), js(js) 
      {}

      void update() {
          js.readPosition();
          int baseSpeed;
          
          if (js.yPos == 0 && js.xPos == 0) {
              leftMotor.stop();
              rightMotor.stop();
          } else if (abs(js.yPos) > abs(js.xPos)) {
              baseSpeed = map(abs(js.yPos), 0, 512, 0, maxMotor);
              if (js.yPos < 0) moveForward(baseSpeed);
              else moveBackward(baseSpeed);
          } else {
              baseSpeed = map(abs(js.xPos), 0, 512, 0, maxMotor);
              if (js.xPos < 0) turnLeft(baseSpeed);
              else turnRight(baseSpeed);
          }
      }
};



Motor leftMotor(10, 8, 7);
Motor rightMotor(9, 6, 5);
JoyStick js(A1, A2);

Platform platform(leftMotor, rightMotor, js);


void setup() {}

void loop() {
  platform.update();
}
