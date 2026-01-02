# Arduino Soil Moisture LCD

Small Arduino Uno project that reads a soil moisture sensor and shows the status on a 16x2 I2C LCD:
"Status:" on the first row and "Soil is DRY / OK / WET" on the second row based on calibrated thresholds.

## Features

- Reads analog soil moisture sensor on A0 and maps raw ADC values from 0-100%.
- Classifies mositure into three states: DRY, OK, WET
- Displays current status on an I2C HD44780 16x2 LCD
- Prints raw reading and percentage to the Serial Monitor

## Hardware

- Arduino Uno
- 16x2 HD44780 LCD with I2C backpack 
- Analog capacitive soil moisture sensor

## Wiring

- LCD:
    - SDA -> A4
    - SCL -> A5
    - VCC -> 5V
    - GND -> GND
- Soil moisture sensor:
    - VCC -> 5V
    - GND -> GND
    - A0 -> A0

## Usage

1. Clone this repo and open the `.ino` file in Arduino IDE or VS Code + Arduino extension.
2. Select your board and port, then upload the sketch.  
3. Open **Serial Monitor** at 9600 baud to see raw readings and calculated moisture percentage.  
4. Insert the probe into your plant’s soil:
   - Measure raw value in very dry soil and very wet soil.  
   - Update `raw_dry` and `raw_wet` in the code to match your readings for better calibration.

## Calibration notes

The percentage shown is a relative value based on your chosen `raw_dry` and `raw_wet` points; it is not an absolute volumetric water content measurement. 
Adjust the `dry` and `wet` thresholds to match what you consider “time to water” and “fully wet” for each plant type 
