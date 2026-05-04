#include "funshield.h"

constexpr int POWERS[] = {1, 10, 100, 1000, 10000};
constexpr int DISPLAY_SIZE = 4;

int getDigit(int num, int pos){
  int digit = (num % POWERS[pos + 1]) / POWERS[pos];

  return digit;
}

class Button{
  private:
    int pin;
    bool lastState;

  public:
    Button(int buttonPin){
      pin = buttonPin;
      lastState = false;
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

class Display{
  private:
    int currentNumber;
    int currentDecimalPos;
    int position;

  public:
    Display(){
      currentNumber = 0;
      currentDecimalPos = 0;
      position = 0;
    }

    void setNumber(int number, int decimalPos){
      currentNumber = number;
      currentDecimalPos = decimalPos;
    }

    void displayNumber(int number, int decimalPos){
      int digit = getDigit(number, position);
      byte glyph = SEG7_DIGIT_GLYPHS[digit];
      
      if (position == decimalPos && decimalPos != 0){
        glyph &= 0x7f;
      }

      shiftOut(SEG7_DATA_PIN, SEG7_CLOCK_PIN, MSBFIRST, glyph);

      int mask = 1 << (DISPLAY_SIZE - position - 1);

      shiftOut(SEG7_DATA_PIN, SEG7_CLOCK_PIN, MSBFIRST, mask);

      digitalWrite(SEG7_LATCH_PIN, LOW);
      digitalWrite(SEG7_LATCH_PIN, HIGH);

      position = (position + 1) % DISPLAY_SIZE;
    }

    void loop(){
      displayNumber(currentNumber, currentDecimalPos);
    }
};

Button incButton(BUTTON1_PIN);
Button decButton(BUTTON2_PIN);
Display display;
Button decimalButton(BUTTON3_PIN);

int number = 0;
int position = 0;
int decimalPosition = 0;

void setup(){
  pinMode(SEG7_LATCH_PIN, OUTPUT);
  pinMode(SEG7_CLOCK_PIN, OUTPUT);
  pinMode(SEG7_DATA_PIN, OUTPUT);

  incButton.begin();
  decButton.begin();
  decimalButton.begin();
}


void loop(){
  
  if (incButton.wasPressed()){
    number = (number + POWERS[position]) % POWERS[DISPLAY_SIZE];
  }
  if (decButton.wasPressed()){
    number = ((number - POWERS[position]) + POWERS[DISPLAY_SIZE]) % POWERS[DISPLAY_SIZE];
  }
  if (decimalButton.wasPressed()){
    decimalPosition = (decimalPosition + 1) % DISPLAY_SIZE;
  }  

  display.setNumber(number, decimalPosition);

  display.loop();
}