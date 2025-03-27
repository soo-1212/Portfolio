#include <Adafruit_LiquidCrystal.h>

int seconds = 0;
Adafruit_LiquidCrystal lcd_1(0);

unsigned long previousMillis = 0;
unsigned long previousMillis2 = 0;
const long interval = 1000;  


void setup()
{
  Serial.begin(9600);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(3, INPUT);
  pinMode(2, INPUT);
  
  lcd_1.begin(16, 2);

  lcd_1.print("distance");
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

  unsigned long currentMillis = millis(); 
  
  
  if (cm > 300) {
    // 아무 것도 하지 않음 (pass)
  } else if (300 >= cm && cm > 200) {
    if (currentMillis - previousMillis >= 500) {
    	previousMillis = currentMillis;
        tone(7, 329, 100); // play tone 60 (C5 = 523 Hz)
    }
  } else if (200 >= cm && cm > 100) {
    if (currentMillis - previousMillis >= 400) {
    	previousMillis = currentMillis;
        tone(7, 329, 100); // play tone 60 (C5 = 523 Hz)
    }
  } else if (100 >= cm && cm > 50) {
    if (currentMillis - previousMillis >= 300) {
    	previousMillis = currentMillis;
        tone(7, 329, 100); // play tone 60 (C5 = 523 Hz)
    }
  } else  {
    if (currentMillis - previousMillis >= 200) {
    	previousMillis = currentMillis;
        tone(7, 329, 100); // play tone 60 (C5 = 523 Hz)
    }
  }

  
  
  Serial.println(cm);
  
  //----------------------------------------------------------------
  int door_safe_butten = digitalRead(3);
  
  int acceleration_pedal = digitalRead(2);
  
  unsigned long currentMillis2 = millis();
  
  if (door_safe_butten == LOW && acceleration_pedal == HIGH){
    digitalWrite(8, HIGH);
    
    if (currentMillis2 - previousMillis2 >= 300) {
    	previousMillis2 = currentMillis2;
        tone(7, 440, 200);
    }
  
  }
  else 
    digitalWrite(8, LOW);
  //----------------------------------------------------------
  
  lcd_1.setCursor(0, 1);
  lcd_1.print(cm);
  if (cm > 300) {
  	  lcd_1.setBacklight(0);
  } else if (300 >= cm ) {
  	  lcd_1.setBacklight(1);
  }
}