/*
This script was used to test the radio communication interface for the RC rover project.
- Jackson Ballew
*/

/*#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7,8); // CE, CSN

const byte address[6] = "00001";

struct point {
    int x;
    int y;
};

void setup(void){
    Serial.begin(9600);
    radio.begin();
    radio.openReadingPipe(1, address);
    radio.setPALevel(RF24_PA_MIN);
    radio.startListening();
}

void loop(void){
    if (radio.available()){
        point data;
        radio.read(&data, sizeof(data));

        // Print the data to the console
        Serial.print("Received point data: X=");
        Serial.print(data.x);
        Serial.print(", Y=");
        Serial.println(data.y);
    }
}*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7,8); // CE, CSN

const byte address[6] = "00001";

struct point {
    int x;
    int y;
};

void setup(void){
    Serial.begin(9600);
    radio.begin();
    radio.openReadingPipe(1, address);
    radio.setPALevel(RF24_PA_MIN);
    radio.startListening();
}

void loop(void){
    if (radio.available()){
        point data;
        radio.read(&data, sizeof(data));
        
        //Send the data to serial port
        Serial.print(data.x);
        Serial.print(",");
        Serial.println(data.y);
    }
}
