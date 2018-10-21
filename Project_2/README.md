# Temperature and Relative Humidity dashboard using Qt, Python, and Websockets

Project 2 for ECEN 5053 (Embedded Interface Design) involved creating a HTML dashboard for displaying temperature and humidity values read from a DHT22 sensor.
The server-side UI was created using Qt Designer, pyuic5, Python, and pyqt5, and it displays timestamped measuements of the current, max, min, and average
temperature and relative humidity. A second server-side script uses Tornado to make a websocket-based client connection and service user requests by providing
the appropriate data. The client-side UI was designed as a simple webpage that connects to the server Pi, and has buttons via which the user can request measured
data. The server and client were implemented on two different Raspberry Pi 3 (Model B) SBCs.

## Author

Shiril Tichkule and Jeet Baru

## Project Work

* **Shiril Tichkule** - *Server-side UI, computing temp/RH statistics, creating CSV datastore for servicing client requests*
* **Jeet Baru** - *Server-side Python script for serving client requests, client-side HTML UI to request and display data*

## Installation Instructions

Clone the project repository using:

```
git clone https://github.com/stichkule/eid-fall2018.git
```

Navigate to the <Project_2> directory:
    
```
cd eid-fall2018/Project_2
```

## Running the application

1. Issue the following from a Bash shell to start data collection and server-side UI:

```
sudo python3 temp_rh_app.py
```

2. Login credentials for server-side UI:

```
username: root
password: 5053
```

3. In a new Bash shell, start the server-side Python script:

```
sudo python3 server.py
```

4. Note the IP of the  server-side interface (eth0 or wlan0) over which the client connection will be made:

```
ifconfig -a
```

5. Copy over the client.html file to the client board, and open it using a web browser.

6. Credentials for making the connection:

```
Username: root
Password: 5053
host: <IP address from Step 4>
port: 8888
URI: /ws
```

## Project Additions

* Option to display temperature in deg C and F (both, server-side and client-side)
* Configurable periodic interval for automated fetching sensor data
* Login screen to secure the application (both, server-side and client-side)

## References

* https://github.com/adafruit/Adafruit_Python_DHT
* https://wiki.python.org/moin/PyQt/Threading%2C_Signals_and_Slots
* https://os.mbed.com/cookbook/Websockets-Server
* https://stackoverflow.com/questions/3163070/javascript-displaying-a-float-to-2-decimal-places
* https://stackoverflow.com/questions/15839169/how-to-get-value-of-selected-radio-button
* https://www.w3schools.com/jsref/jsref_parsefloat.asp
* https://stackoverflow.com/questions/763745/how-to-get-text-box-value-in-javascript
* https://pythonspot.com/files-spreadsheets-csv/
* https://stackoverflow.com/questions/30357663/tornado-ioloop-threading