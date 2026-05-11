void setup() {
  // put your setup code here, to run once:

  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(2, HIGH);
  delay(250); //ms

  digitalWrite(2, LOW);
  delay(250); //ms

}
