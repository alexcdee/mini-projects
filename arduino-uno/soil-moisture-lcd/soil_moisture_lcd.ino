#include <Wire.h> // I2C bus support
#include <hd44780.h> // Core hd4478 LCD library
#include <hd44780ioClass/hd44780_I2Cexp.h> // I2C backpack driver


// LCD object (I2C)
hd44780_I2Cexp lcd;


// analog pin for soil moisture sensor
const int moisture_pin = A0;


// calibration points: approx. raw ADC values for the soil
const int raw_dry = 800; // read in dry soil
const int raw_wet = 300; // read in wet soil

// thresholds in % values used to measure the moisture
const int dry = 30; // below = dry
const int wet = 70; // above = wet

// update status @ 2 seconds each interval
const unsigned long update_interval_ms = 2000;
unsigned long lastUpdate = 0;


// convert raw analog value to 0-100 % moisture values
int rawToPercent(int raw) {
  if (raw_dry == raw_wet) return 0;

  int percent = map(raw, raw_dry, raw_wet, 0, 100);

  if (percent < 0) percent = 0;
  if (percent > 100) percent = 100;
  return percent;
}


void setup() {

  Serial.begin(9600); // match the Serial Monitor


  int status = lcd.begin(16, 2);

  // set up the lcd screen
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Status:");
  lcd.setCursor(0,1);
  lcd.print("Reading level"); 
}


void loop() {
 
  // update readings every interval @ 2 seconds
  unsigned long now = millis();   
  if (now - lastUpdate >= update_interval_ms) {
    lastUpdate = now;
  
    // read raw analog sensor value
    int raw = analogRead(moisture_pin); 
    // convert raw reading into % 
    int moisturePercent = rawToPercent(raw);


    const char* status;
    if (moisturePercent <= dry) {        
      status = "Soil is DRY";
    } else if (moisturePercent >= wet) { 
      status = "Soil is WET";
    } else {
      status = "Soil is OK";
    }

    // log readings to Serial Monitor
    Serial.print("Raw: ");
    Serial.print(raw);
    Serial.print("Moisture: ");
    Serial.print(moisturePercent);
    Serial.print("% -> ");
    Serial.println(status);

    // update the status level
    lcd.setCursor(0,1);
    lcd.print("                ");
    lcd.setCursor(0,1);
    lcd.print(status);


  }
}
