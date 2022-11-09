int pEMG_0 = A0;
int pEMG_1 = A1;
int pEMG_2 = A2;

int aEMG_0;
int aEMG_1;
int aEMG_2;
   
void setup() 
{
  Serial.begin(9600);
}

void loop()
{
  aEMG_0 = analogRead(pEMG_0);
  aEMG_1 = analogRead(pEMG_1);
  aEMG_2 = analogRead(pEMG_2);


 // Serial.print(millis());
 // Serial.print(",");   
  Serial.print(aEMG_0);
  Serial.print(",");
  Serial.print(aEMG_1);
  Serial.print(",");
  Serial.print(aEMG_2);
  Serial.print(",");
  Serial.println();
  //delayMicroseconds(950);
  delay(10);
}
