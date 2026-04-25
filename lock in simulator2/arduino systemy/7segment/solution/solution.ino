#include "funshield.h"

constexpr int powers[] = {1, 10, 100, 1000, 10000};

class Button{
  private:
    int pin;
    bool lastState;
    int currentDigit;

  public:
    Button(int buttonPin){
      pin = buttonPin;
      currentDigit = 0;
    }

    void begin(){
      pinMode(pin, INPUT);
    }

    bool wasPressed() {
      bool isPressed = (digitalRead(pin) == ON);

      if (isPressed != lastState) {
        lastState = isPressed;
        if (isPressed) {
          return true;
        }
      }
      return false;
    }
};

int getDigit(int num, int pos){
  int digit = (num % powers[pos + 1]) / powers[pos];

  return digit;
}

void displayNumber(int digit, int position){
  shiftOut(SEG7_DATA_PIN, SEG7_CLOCK_PIN, MSBFIRST, SEG7_DIGIT_GLYPHS[digit]);

  position = 8 >> position;

  shiftOut(SEG7_DATA_PIN, SEG7_CLOCK_PIN, MSBFIRST, position);

  digitalWrite(SEG7_LATCH_PIN, LOW);
  digitalWrite(SEG7_LATCH_PIN, HIGH);
}

Button incButton(BUTTON1_PIN);
Button decButton(BUTTON2_PIN);
Button digitButton(BUTTON3_PIN);

void setup(){
  pinMode(SEG7_LATCH_PIN, OUTPUT);
  pinMode(SEG7_CLOCK_PIN, OUTPUT);
  pinMode(SEG7_DATA_PIN, OUTPUT);

  incButton.begin();
  decButton.begin();
  digitButton.begin();
}

int number = 0;
int position = 0;

void loop(){
  
  if (incButton.wasPressed()){
    number = (number + powers[position]) % 10000;
  }
  if (decButton.wasPressed()){
    number = (number - powers[position]) + 10000;

  }
  if (digitButton.wasPressed()){
    position = (position + 1) % 4;
  }
  

  displayNumber(getDigit(number, position), position);
}