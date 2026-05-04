#include "funshield.h"

constexpr int POWERS[] = {1, 10, 100, 1000, 10000};
constexpr int DISPLAY_SIZE = 4;

class Button{
  private:
    int pin;
    bool lastState;

  public:
    Button(int buttonPin){
      pin = buttonPin;
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
  int digit = (num % POWERS[pos + 1]) / POWERS[pos];

  return digit;
}

void displayNumber(int digit, int position){
  shiftOut(SEG7_DATA_PIN, SEG7_CLOCK_PIN, MSBFIRST, SEG7_DIGIT_GLYPHS[digit]);

  int mask = (1 << (DISPLAY_SIZE - position - 1));

  shiftOut(SEG7_DATA_PIN, SEG7_CLOCK_PIN, MSBFIRST, mask);

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
    number = (number + POWERS[position]) % POWERS[DISPLAY_SIZE];
  }
  if (decButton.wasPressed()){
    number = ((number - POWERS[position]) + POWERS[DISPLAY_SIZE]) % POWERS[DISPLAY_SIZE];

  }
  if (digitButton.wasPressed()){
    position = (position + 1) % DISPLAY_SIZE;
  }
  displayNumber(getDigit(number, position), position);

}