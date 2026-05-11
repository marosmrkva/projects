#include "funshield.h"

constexpr int POWERS[] = {1, 10, 100, 1000, 10000};
constexpr int DISPLAY_SIZE = 4;

enum State{
  stopped,
  running,
  lapped
};

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

class Timer{
  private:
    State currentState;
    unsigned long elapsedTime = 0;
    unsigned long lastTime = 0;
    unsigned long frozenLapTime;

  public:
    Timer(){
      currentState = stopped;
    } 

    void loop(bool b1Pressed, bool b2Pressed, bool b3Pressed){

      unsigned long currentTime = millis();
      unsigned long deltaTime = currentTime - lastTime;
      lastTime = currentTime;

      if (currentState == running || currentState == lapped){
        elapsedTime += deltaTime;
      }   

      if (b1Pressed){
        if (currentState == stopped){
          currentState = running;
        }
        else if (currentState == running){
          currentState = stopped;
        }
      }

      if (b2Pressed){
        if (currentState == running){
          currentState = lapped;
          frozenLapTime = elapsedTime;
        }
        else if (currentState == lapped){
          currentState = running;
        }
      }

      if (b3Pressed){
        if (currentState == stopped){
          currentState = stopped;
          elapsedTime = 0;
        }
      }
    }

    int getDisplayTime(){
      if (currentState == running ||currentState == stopped){
        return elapsedTime / 100;
      }
      else if (currentState == lapped){
        return frozenLapTime / 100;
      }
      return 0;
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

      if (position > decimalPos && number < POWERS[position]){
        glyph = SEG7_EMPTY_GLYPH;
      }

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

Button startButton(BUTTON1_PIN);
Button lapButton(BUTTON2_PIN);
Button resetButton(BUTTON3_PIN);
Display display;
Timer timer;

void setup(){
  pinMode(SEG7_LATCH_PIN, OUTPUT);
  pinMode(SEG7_CLOCK_PIN, OUTPUT);
  pinMode(SEG7_DATA_PIN, OUTPUT);

  startButton.begin();
  lapButton.begin();
  resetButton.begin();
}

void loop(){
  bool b1 = startButton.wasPressed();
  bool b2 = lapButton.wasPressed();
  bool b3 = resetButton.wasPressed();

  timer.loop(b1, b2, b3);
  display.setNumber(timer.getDisplayTime(), 1);
  display.loop();
}