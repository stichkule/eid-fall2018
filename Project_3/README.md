# Temperature and Relative Humidity dashboard using Qt, Python, AWS IoT, MQTT, and SQS

Project 3 for ECEN 5053 (Embedded Interface Design) involved creating server-side and client-side Qt dashboards for displaying temperature and humidity values read from a DHT22 sensor.
Both UIs were created using Qt Designer, pyuic5, Python, and pyqt5, and they display timestamped measuements of the current, max, min, and average temperature and relative humidity.
The server and client were implemented on two different Raspberry Pi 3 (Model B) SBCs. The server-side Raspberry Pi (temp_rh_app.py) measures temperature and relative humidity at
5-s intervals, computes their relevant statistics, and stores them in a CSV file. A second server-side script (basicPubSub.py) reads this CSV file, and publishes the contained
data via MQTT to a AWS IoT thing subscribed to the topic sdk/test/Python.

On the AWS side, a lambda function was created that triggers upon each message reception, and writes the JSON data into a SQS FIFO queue. The client-side Raspberry Pi (temp_rh_app.py)
uses a BOTO3 client to interface with, and read messages from the SQS queue. The temperature and relative humidity data read from the messages are used to populate a UI similar to that
of the server. Further, time series of the measured temperature and relative humidity along with their statistics are also plotted using matplotlib on the client-side UI.

## Author

Shiril Tichkule and Jeet Baru

## Project Work

* **Shiril Tichkule** - *Server-side UI, computing temp/RH statistics, creating CSV datastore, MQTT messaging, AWS IoT Thing configuration*
* **Jeet Baru** - *Lambda function, AWS IoT Thing and SQS queue configuration, client-side UI, data plotting*

## Installation Instructions

Clone the project repository using:

```
git clone https://github.com/stichkule/eid-fall2018.git
```

Navigate to the <Project_3> directory:
    
```
cd eid-fall2018/Project_3
```

## Running the application -- Server

1. Navigate to the Server folder:

```
cd Server
```

2. Issue the following from a Bash shell to start data collection and server-side UI:

```
sudo python3 temp_rh_app.py
```

3. Login credentials for server-side UI:

```
username: root
password: 5053
```

4. In a new Bash shell, launch the script that initiates MQTT messaging to the AWS IoT Thing:

```
./start.sh
```

## Running the application -- Client

1. Wait for a couple of minutes until the SQS queue is populated, and then navigate to the Client folder:

```
cd Client
```

2. Launch the client-side UI (without sudo):
    
```
python3 temp_rh_app.py
```

3. Login credentials for client-side UI:

```
username: root
password: 5053
```

## Project Additions

* Login screen to secure the application (both, server-side and client-side)

## References

* https://github.com/adafruit/Adafruit_Python_DHT
* https://wiki.python.org/moin/PyQt/Threading%2C_Signals_and_Slots
* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-example-sending-receiving-msgs.html
* https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples-send-receive-messages.html
* https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-tutorials-configure-queues.html
* https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html
* https://stackoverflow.com/questions/40992950/read-a-csv-file-and-put-its-content-into-a-python-list
