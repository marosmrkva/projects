#include "SevSeg.h"

SevSeg sevseg; 

void setup() {
  byte numDigits = 4;
  // Piny pre D1, D2, D3, D4 (podľa tabuľky vyššie)
  byte digitPins[] = {10, 11, 12, 13}; 
  // Piny pre segmenty A, B, C, D, E, F, G, DP
  byte segmentPins[] = {2, 3, 4, 5, 6, 7, 8, 9}; 
  
  bool resistorsOnSegments = true; // Máme rezistory na pinoch segmentov
  byte hardwareConfig = COMMON_ANODE; // Tvoj HSN-5461BS je Common Anode
  
  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments);
  sevseg.setBrightness(90);
}

void loop() {
  // Zobrazí číslo 1234
  sevseg.setNumber(501);
  
  // Refresh musí byť v loop bez delay, aby fungovalo multiplexovanie
  sevseg.refreshDisplay(); 
}