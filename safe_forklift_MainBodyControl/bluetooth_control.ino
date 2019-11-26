#include <SoftwareSerial.h>

SoftwareSerial BTSerial(2, 3); 
// SoftwareSerial(RX, TX)


int LeftMotor = 12;
int LeftMotor_pwm = 10;
int RightMotor = 13;
int RightMotor_pwm = 11;

int value = 77;

void setup() {
  // put your setup code here, to run once:
  BTSerial.begin(9600);
  Serial.begin(9600);
  
  pinMode(LeftMotor, OUTPUT);
  pinMode(LeftMotor_pwm, OUTPUT);
  pinMode(RightMotor, OUTPUT);
  pinMode(RightMotor_pwm, OUTPUT);
}
void back(){

  digitalWrite(LeftMotor, HIGH);
  analogWrite(LeftMotor_pwm, value);
  digitalWrite(RightMotor, HIGH);
  analogWrite(RightMotor_pwm, value);
  
}

void go(){

  digitalWrite(LeftMotor, LOW);
  analogWrite(LeftMotor_pwm, value);
  digitalWrite(RightMotor, LOW);
  analogWrite(RightMotor_pwm, value);
  
}

void right(){
  
  digitalWrite(LeftMotor, LOW);
  analogWrite(LeftMotor_pwm, value);
  digitalWrite(RightMotor, HIGH);
  analogWrite(RightMotor_pwm, value);
  
}
void left(){

  digitalWrite(LeftMotor, HIGH);
  analogWrite(LeftMotor_pwm, value);
  digitalWrite(RightMotor, LOW);
  analogWrite(RightMotor_pwm, value);
  
}

void allstop(){
  
  //digitalWrite(LeftMotor, LOW);
  digitalWrite(LeftMotor_pwm, LOW);
  //digitalWrite(RightMotor, LOW);
  digitalWrite(RightMotor_pwm, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(BTSerial.available()){
    char data = BTSerial.read();
    Serial.println(data);
    switch(data){
      case 'G' :
         go();
         break;
      case 'L' :
         left();
         break;
      case 'R' :
         right();
         break;
      case 'B' :
         back();
         break;
      case 'S':
         allstop();
         break;
      case 'd':
         value -= 5;
         break;
      case 'u':
        value += 5;
        break;
    }
  }
}
