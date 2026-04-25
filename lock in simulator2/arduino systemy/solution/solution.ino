#include "funshield.h"

unsigned long lastTime;
unsigned long timer;
constexpr long INTERVAL = 300;

constexpr int LED_PINS[] = {LED1_PIN, LED2_PIN, LED3_PIN, LED4_PIN};
constexpr int LEDS_SIZE = sizeof(LED_PINS)/sizeof(LED_PINS[0]);
unsigned int currentLED = 0;
bool isMovingForward = false;

void setup() {
  for (int i = 0; i < LEDS_SIZE; i++){
    pinMode(LED_PINS[i], OUTPUT);
  }

  lastTime = millis();
  timer = 0;
}

void moveLed(){
  if (isMovingForward){
    currentLED -= 1;
  }
  else{
    currentLED += 1;
  }
}

void animationStep(){
  for (int checkedLED = 0; checkedLED < LEDS_SIZE; checkedLED++){
      if (checkedLED != currentLED){
        digitalWrite(LED_PINS[checkedLED], OFF);
      }
      else{
        digitalWrite(LED_PINS[checkedLED], ON);
      }
    }
  moveLed();
}

void changeDirection(){
  if (currentLED == 0 || currentLED == LEDS_SIZE - 1){
    isMovingForward = !isMovingForward;
  }
}

int animate(){
  if (timer >= INTERVAL){
    timer -= INTERVAL;
    animationStep();
    changeDirection();
  }
  return timer;
}

void loop() {
  unsigned long currentTime = millis();
  unsigned long deltaTime = currentTime - lastTime;

  lastTime = currentTime;
  timer += deltaTime;

  animate();


}
