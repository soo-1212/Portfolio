
void setup()
{
  Serial.begin(9600);
  pinMode(7, OUTPUT);
}

void loop()
{
  
  pinMode(9, OUTPUT);
  digitalWrite(9,LOW);
  delayMicroseconds(2);
  digitalWrite(9,HIGH);
  delayMicroseconds(5);
  digitalWrite(9,LOW);
  
  
  pinMode(9, INPUT);
  double duration = pulseIn(9, HIGH);
  double cm = duration * 340 / 10000 / 2 ;

  if (cm > 300) {
      tone(7, 523, 100); // play tone 60 (C5 = 523 Hz)
      delay(700); 
  } else if (300 >= cm && cm > 200) {
      tone(7, 523, 100); // play tone 60 (C5 = 523 Hz)
      delay(500); 
  } else if (200 >= cm && cm > 100) {
      tone(7, 523, 100); // play tone 60 (C5 = 523 Hz)
      delay(300); 
  } else  {
      tone(7, 523, 100); // play tone 60 (C5 = 523 Hz)
      delay(200); 
  }

  
  
  Serial.println(cm);
  
}