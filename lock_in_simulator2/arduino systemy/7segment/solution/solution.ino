#include "funshield.h"

constexpr int powers[] = {1, 10, 100, 1000, 10000};

class Button{
  private:
    int pin;
    bool lastState; //posledny stav tlacidla
    unsigned long lastActionTime; //cas poslednej smeny stavu
    int holdPhase; //faza/stav stlacenia tlacidla
    int currentDigit;

  public:
    Button(int buttonPin){
      pin = buttonPin;
      currentDigit = 0;
    }

    void begin(){
      pinMode(pin, INPUT);
    }

    int changeDigit(){
      bool isPressed = (digitalRead(pin) == ON); //aktualny stav tlacidla
      
      if (!isPressed){
        lastState = isPressed;
      }

      if (isPressed && !lastState){
        currentDigit++;

        lastState = isPressed;
      }

      return currentDigit % 4;
    }

    int incDigit(int num){
      num = num + (1 * powers[currentDigit + 1] / powers[10]);

      return num;
    }

    int decDigit(){
      num = num - (1 * powers[currentDigit + 1] / powers[10]);

      return num;
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

void loop(){
  
  int position = digitButton.changeDigit();

  displayNumber(getDigit(1234, position), position);



}