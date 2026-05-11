#include "funshield.h"

constexpr int LED_PINS[] = {LED1_PIN, LED2_PIN, LED3_PIN, LED4_PIN};
constexpr int LEDS_SIZE = sizeof(LED_PINS)/sizeof(LED_PINS[0]);

unsigned int currentValue = 1;

bool button1_state = OFF;
bool button2_state = OFF;


void setup() {
  for (int i = 0; i < LEDS_SIZE; i++){
    pinMode(LED_PINS[i], OUTPUT);
    digitalWrite(LED_PINS[i], OFF);
  }

  pinMode(BUTTON1_PIN, INPUT);
}


void displayNumber(int number) {
  for (int i = 0; i < LEDS_SIZE; i++){
    if ((number & (1<<i)) > 0){
      digitalWrite(LED_PINS[i], ON);
    }
    else{
      digitalWrite(LED_PINS[i], OFF);
    }
  }
}


void loop() {

  button1_state = digitalRead(BUTTON1_PIN);
  button2_state = digitalRead(BUTTON2_PIN);

  if (button1_state == ON){
    currentValue++;
    currentValue = currentValue%(1<<LEDS_SIZE);
    displayNumber(currentValue);
    delay(1000);
  }

  if (button2_state == ON){
    
    currentValue--;
    currentValue = currentValue%(1<<LEDS_SIZE);
    displayNumber(currentValue);
    delay(1000);
  }
  
  
  
}
