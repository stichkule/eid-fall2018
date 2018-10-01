# Dashboard for Temperature and Relative Humidity monitoring

Project 1 for ECEN 5053 (Embedded Interface Design) involved creating a dashboard for displaying temperature and humidity values read from a DHT22 sensor.
The UI was created using Qt Designer, and converted into Python using pyuic5. The underlying app functionality was designed in Python using pyqt5.
The implementation platform was a Raspberry Pi 3 (Model B) SBC.

## Author

Shiril Tichkule

## Project Work

* **Shiril Tichkule** - *Developed all parts*

## Installation Instructions

Clone the project repository using:

```
git clone https://github.com/stichkule/eid-fall2018.git
```

Navigate to the <Project_1> directory:
    
```
cd eid-fall2018/Project_1
```

## Running the application

Issue the following from a Bash shell:

```
sudo python3 temp_rh_app.py
```
Credentials for login screen: username = root; password = 5053

## Project Additions

* Option to display temperature in deg C and F
* Configurable periodic interval for automated fetching sensor data
* Setting thresholds and activating temperature and relative humidity alarms
* Plotting time series of fetched data
* Login screen to secure the application

## References

* https://wiki.python.org/moin/PyQt/Tutorials
* https://www.hackster.io/adamgarbo/raspberry-pi-2-iot-thingspeak-dht22-sensor-b208f4
* https://github.com/adafruit/Adafruit_Python_DHT
* https://wiki.python.org/moin/PyQt/Threading%2C_Signals_and_Slots
* https://gist.github.com/MalloyDelacroix/2c509d6bcad35c7e35b1851dfc32d161
* https://www.baldengineer.com/raspberry-pi-gui-tutorial.html
* https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
