#include<Servo.h>
//#include <SoftwareSerial.h>

#define DIST_S 55*58.2 // 100cm로 제한
#define PING_INTERVAL 6// Milliseconds // 4개의 경우 60ms
#define MAX  55

//SoftwareSerial BT(2,3);
const int servoPin = 12;
Servo myServo;
int servoPos = 0;
bool posIncrease = true;

int trig[4] = {6, 4, 8, 10}; //FLRB
int echo[4] = {7, 5,9 ,11}; //FLRB
uint8_t currentSensor = 0;
unsigned long pingTimer[4];
long dist_r[4];
int count;
void setup() {
  Serial.begin (9600);
  myServo.attach(servoPin);
  for (int i = 0; i <= 3; i++) {
    pinMode(trig[i], OUTPUT);
    pinMode(echo[i], INPUT);
  }
  for (uint8_t i = 1; i < 4; i++)
    pingTimer[i] = pingTimer[i - 1] + PING_INTERVAL;
}
long times = millis();
void loop() {
  for (int i = 0; i <= 3; i++) {
    if (millis() >= pingTimer[i]) {
      pingTimer[i] += PING_INTERVAL * 4;
      if (i == 0 && currentSensor == 3)
        oneSensorCycle();
      currentSensor = i;
      dist_r[i] = trig_ultra(trig[i], echo[i]);
      if (dist_r[i] == 0) {
        dist_r[i] = MAX;
      }
    }
  }
  // 원하는 코드 추가
}

long trig_ultra(int TRIG, int ECHO)
{
  long dist;
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  dist = pulseIn(ECHO, HIGH, DIST_S) / 58.2;
  return (dist);
}
void oneSensorCycle() {
  Serial.println(String(servoPos)+"#"+String(dist_r[0]) + "#" + String(dist_r[1]) + "#" + String(dist_r[2]) + "#" + String(dist_r[3]));
  if (posIncrease) {
    myServo.write(servoPos++);
    if (servoPos == 180) {
      posIncrease = false;
    }
  }
  else {
    myServo.write(servoPos--);
    if (servoPos == 0) {
      posIncrease = true;
    }
  }
}
