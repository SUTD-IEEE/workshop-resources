int led=13;

void setup() 
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() 
{
  if (Serial.available() > 0)
  {
    int incomingbyte = Serial.read();

    switch(incomingbyte) 
    {
      case '1':
        digitalWrite(13, HIGH);
        Serial.println("lighting up");
        delay(100);
        break;
       case '2':
        digitalWrite(13, LOW);
        Serial.println("powering down");
        delay(100);
        break;
       default:
        break;
      }
    }
}

