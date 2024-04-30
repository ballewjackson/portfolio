/*
This sketch plays various chimes using a buzzer on attatched to an arduino.
Current program structure blocks other actions which is not ideal.

- Jackson Ballew
*/


int buzzerpin = 6;

void playToneSequence(int *notes, int *durations, int length) {
  for (int i = 0; i < length; i++) {
    tone(buzzerpin, notes[i], durations[i]);
    delay(durations[i] + 10); // Short pause between notes
    noTone(buzzerpin);
  }
}

void sound1() {
  int notes[] = {494, 2*494, 494, 2*494, 2*466, 494, 2*466, 740}; 
  int durations[] = {140, 140, 140, 140, 140, 140, 140, 140};
  playToneSequence(notes, durations, 8);
}

void sound2() {
  //int notes[] = {554, 784, 554, 784, 554, 784, 554, 784, 554, 784}; 
  //int durations[] = {50, 50, 50, 50, 50, 50, 50, 50, 50, 50};
  //playToneSequence(notes, durations, 10);

  for (int i = 0; i < 7; i++) {
    int notes[] = {554, 784}; 
    int durations[] = {50, 50};
    playToneSequence(notes, durations, 2);
  }
}

void sound3() {
  int notes[] = {0.5 * 523, 523, 2* 523};
  int durations[] = {100, 100, 100};
  playToneSequence(notes, durations, 3);
}

void sound4() {
  int notes[] = {523, 523};
  int durations[] = {100, 100};
  playToneSequence(notes, durations, 2);
}

void setup() {

}

void loop() {
  sound1();
  delay(2000);
  sound2();
  delay(2000);
  sound3();
  delay(2000);
  sound4();
  delay(2000);
}