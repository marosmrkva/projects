#include "funshield.h"
#include <math.h>

unsigned long lastTime;
unsigned long timer;

constexpr int LED_PINS[] { LED1_PIN, LED2_PIN, LED3_PIN, LED4_PIN };
constexpr int LED_PINS_COUNT = sizeof(LED_PINS) / sizeof(LED_PINS[0]);

constexpr int ACTIVATION_DELAY = 1000; // how long before button starts to perform periodic updates [ms]
constexpr int PERIODIC_DELAY = 300; // delay between consecutive periodic updates [ms]

int currentNumber = 0; //aktualne zobrazena hodnota
constexpr int maxLedValue = (2 << LED_PINS_COUNT);

//mozne stavy tlacidla
enum Phase{
  released, //tlacidlo nie je stlacene
  pressed, //tlacidlo bolo prvykrat stlacene
  held //tlacidlo je drzane po prvom stlaceni
};

class Button{
  private:
    int pin;
    bool lastState; //posledny stav tlacidla
    unsigned long lastActionTime; //cas poslednej smeny stavu
    int holdPhase; //faza/stav stlacenia tlacidla

  public:
    Button(int buttonPin){
      pin = buttonPin;
      lastState = OFF;
      lastActionTime = 0;
    }

    void begin(){
      pinMode(pin, INPUT);
    }

    bool wasPressed(){
      bool isPressed = (digitalRead(pin) == ON); //aktualny stav tlacidla
      unsigned long currentTime = millis(); //aktualny cas od spustenia

      if (!isPressed){ 
        //ak tlacidlo nie je stlacene, resetuje sa jeho stav a funkcia vracia false, teda nespusti sa akcia
        lastState = isPressed;
        holdPhase = released;
        return false;
      }

      if (!lastState){
          //ak je tlacidlo stlacene ale pri poslednej kontrole stavu este nebolo
          lastActionTime = currentTime; //aktualizuje sa cas poslednej zmeny
          holdPhase = pressed; //jeho stav sa zmeni na pociatocne stlacenie - pressed
          lastState = isPressed; //posledny stav tlacidla je stlacene (podla citania z pinu)
          return true;
        }
      
      if (holdPhase == pressed && (currentTime - lastActionTime >= ACTIVATION_DELAY)){
        //ak je tlacidlo stale stlacene a stale sme v prvej sekunde stlacenia = pomaly prvy inkrement
        lastActionTime += ACTIVATION_DELAY; //cas poslednej zmeny sa zmeni o sekundu
        holdPhase = held; //faza/stav stlacenia sa zmeni na stale stlacene - held
        return true;
      }
      else if (holdPhase == held && (currentTime - lastActionTime >= PERIODIC_DELAY)){
        lastActionTime += PERIODIC_DELAY; //cas poslednej zmeny sa zmeni o 300ms = rychle inkrementy
        return true;
      }
      
      return false; //ak sa nic nestalo, funkcia vracia false, teda sa nespusti ziadna akcia
    }
};

//nastavenie pinov oboch vstupnych tlacidiel
Button incButton(BUTTON1_PIN);
Button decButton(BUTTON2_PIN);

void displayNumber(int number) {
  //funkcia zobrazi aktualnu hodnotu na ledky v binarnej sustave
  for (int i = 0; i < LED_PINS_COUNT; i++){
    int ledIndex = (LED_PINS_COUNT - 1) - i; //spocitame aktualny index ledky
    bool isLedOn = (number & (1 << i)) > 0; 
    int newLedState = isLedOn ? ON : OFF; //spocitame hodnotu ledky

    digitalWrite(LED_PINS[ledIndex], newLedState);
  }
}

void setup() {
  //inicializacia oboch tlacidiel
  incButton.begin();
  decButton.begin();

  for (int i = 0; i < LED_PINS_COUNT; ++i) {
    //inicializacia pinov lediek
    pinMode(LED_PINS[i], OUTPUT);
    digitalWrite(LED_PINS[i], OFF);
  }

  displayNumber(currentNumber); //zobrazenie pociatocnej hodnoty (0)
}



void loop() {
  if (incButton.wasPressed()){
    //ak je prve tlacidlo stlacene, hodnota sa inkrementuje a zobrazi
    currentNumber = (currentNumber + 1) % maxLedValue;
    displayNumber(currentNumber);
  }

  if (decButton.wasPressed()){
    //naopak pri stlaceni druheho tlacidla sa dekrementuje a zobrazi
    currentNumber = (int) (currentNumber + maxLedValue - 1) % maxLedValue;
    displayNumber(currentNumber);
  }
}
