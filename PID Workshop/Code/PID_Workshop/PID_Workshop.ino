int ENA = 5;
int ENB = 6;
int IN1 = 10;
int IN2 = 11;
int IN3 = 12;
int IN4 = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A1, INPUT);
  pinMode(A0, INPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

float P {0}, I {0}, D {0};

float Kp {15}, Ki {0}, Kd {0};

int black = 500;
int white = 52;

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(analogRead(A5));
  Serial.print('\t');
  Serial.println(analogRead(A4));
  int left_sensor = 1-digitalRead(A0);
  int right_sensor = 1-digitalRead(A1);

//  Serial.print(left_sensor);
//  Serial.print('\t');
//  Serial.print(right_sensor);

  int error = right_sensor - left_sensor;
//  Serial.print('\t');
//  Serial.println(error);
  P = error;
//  moveMotor(1, 30 + Kp * P); // Left motor
//  moveMotor(2, 30 - Kp * P); // Right motor
//  moveMotor(1, 30);
//  moveMotor(2, 30);
}

void moveMotor(int num, int speed) {
  switch (num) {
    case 1:
      if (speed < 0) {
        analogWrite(ENA, map(speed, -100, 0, 255, 0));
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
      } else if (speed > 0) {
        analogWrite(ENA, map(speed, 0, 100, 0, 255));
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
      } else {
        digitalWrite(ENA, LOW);
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
      }
      break;
    case 2:
      if (speed < 0) {
        analogWrite(ENB, map(speed, -100, 0, 255, 0));
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
      } else if (speed > 0) {
        analogWrite(ENB, map(speed, 0, 100, 0, 255));
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
      } else {
        digitalWrite(ENB, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
      }
      break;
  }
}

