# -*- coding: utf-8 -*-
"""
Python code to implement the temperature and relative humidity monitoring application for Project 3 of ECEN 5053.
The GUI for this app was created using Qt Designer and can be found in the file temp_rh_dashboard.ui. This app
interfaces with the GUI using the converted file temp_rh_dashboard.py. Temperature and relative humidity measurements
are made using a DHT22 sensor connected to the Raspberry Pi. The measured data and timestamps are written into a CSV
file as strings, which are then sent to a AWS IoT thing via the MQTT protocol.
The app includes the following functionality:
* Temperature reading in deg C and F
* Configurable periodic interval for fetching sensor data (default of 5 s)
* Display of temperature and humidity statistics (low, high, average values)
* Login screen to secure the application

Running the App: issue the command -- sudo python3 temp_rh_app.py from a Bash shell

@author: Shiril Tichkule, Jeet Baru
@date: 11 November 2018
"""

import sys
import csv
import threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from temp_rh_dashboard import Ui_MainWindow
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22 #sensor name
pin = 4 #GPIO pin number

#Global variables
update_interval = 5 # refresh interval in seconds
unit = 'C' #default temperature units
temp_list=[] #lists for storing temp, rh, and timestamp data for plotting
rh_list=[]
time_list=[]
fmtr = dates.DateFormatter("%H:%M:%S") #date format for timestamp display

temp_high = -40.0; #initial values based on DHT22 datasheet
temp_low = 125.0;
rh_high = 0.0;
rh_low = 100.0;

cntr=0; #no. of measurements for computing statistics

ui=Ui_MainWindow() #initialize app window

class Login(QtWidgets.QWidget):
    """class for creating and implementing login window"""
    switch_window = QtCore.pyqtSignal() #window switch signal

    def __init__(self):
        """constructor to create login window with username and password fields and authenticate button"""
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Authenticate')
        self.username = QtWidgets.QLineEdit()
        self.username.setPlaceholderText('username')
        self.passwd = QtWidgets.QLineEdit()
        self.passwd.setPlaceholderText('password')
        self.button.clicked.connect(self.login)

        layout.addWidget(self.username)
        layout.addWidget(self.passwd)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def login(self):
        """login function that tests entered credentials"""
        if(self.username.text() == 'root' and self.passwd.text() == '5053'):
            self.switch_window.emit() #emit switch signal to invoke main window only if credentials are valid

class Controller:
    """controller class to choose what window must be displayed"""
    def __init__(self):
        pass
    
    def show_login(self):
        """function that displays login window"""
        self.login = Login()
        self.login.switch_window.connect(self.show_main) #show main window if switching signal received
        self.login.show()
        
    def show_main(self):
        """function to implement main window"""
        global ui
        self.window = QDialog()
        ui.setupUi(self.window)
        self.login.close()
        self.window.show()
        update_data() #update data at periodic interval
        ui.radioButton_F.clicked.connect(lambda:change_to_F()) #change units of temperature display
        ui.radioButton_C.clicked.connect(lambda:change_to_degC())
        ui.pushButton_OK.clicked.connect(lambda:update_refresh_interval()) #change periodic refresh interval

def main():
    """main function that invokes controller class methods"""
    app = QApplication(sys.argv) #launch app
    controller = Controller() #launch controller
    controller.show_login() #show login window
    sys.exit(app.exec_()) #exit app
       
def change_to_F():
    """change units from degC to F"""
    global unit
    unit = 'F'
    update_data()

def change_to_degC():
    """change units from F to degC"""
    global unit
    unit = 'C'
    update_data()
    
def update_refresh_interval():
    """change default refresh interval to user-defined value"""
    global update_interval
    refresh_str = ui.text_refresh.toPlainText() #read string from text edit box
    if(refresh_str!=''): #if string not empty, change interval
        update_interval = int(refresh_str)
    update_data()

def update_data(): 
    """function to update temperature, humidity and alarms on display"""
    global temp, temp_low, temp_high, temp_avg, rh, rh_low, rh_high, rh_avg, ts_temp_low, ts_temp_high, ts_rh_low, ts_rh_high, unit, ui, cntr;
    
    data_list=[] #list of recorded data for each measurement
    cntr+=1;
    t = threading.Timer(update_interval,update_data).start() # thread to autorun function once every update interval
    
    rh, temp = Adafruit_DHT.read_retry(sensor, pin) #read sensor data
    timestamp=datetime.now().strftime('%d %b %Y %H:%M:%S') #format timestamp
    ui.label_timestamp.setText(timestamp)
    
    temp_list.append(temp) #append data to lists for computing statistics
    rh_list.append(rh)
    time_list.append(timestamp)
    
    temp_type_str = "C" #default temperature unit
    
    temp_avg = temp; #displaying when only one measurement is made
    rh_avg = rh;
    temp_low = temp;
    rh_low = rh;
    ts_temp_low = timestamp;
    ts_rh_low = timestamp;
    temp_high = temp;
    rh_high = rh;
    ts_temp_high = timestamp;
    ts_rh_high = timestamp;
    
    if(cntr>1): #if more than one measurement, compute statistics
        temp_avg, rh_avg = calc_avg()
        ts_temp_low, ts_rh_low, temp_low, rh_low = calc_low()
        ts_temp_high, ts_rh_high, temp_high, rh_high = calc_high()
    
    temperature_str_csv = "{:.2f}".format(temp) #append temp values in C for CSV file
    temperature_avg_str_csv = "{:.2f}".format(temp_avg)
    temperature_low_str_csv = "{:.2f}".format(temp_low)
    temperature_high_str_csv = "{:.2f}".format(temp_high)
    
    if(unit=='F' and temp!=None): # if unit is set to F, convert from deg C to F
        temp= (temp*1.8) + 32
        temperature_str = "{:.2f}".format(temp)
        temp_avg= (temp_avg*1.8) + 32
        temperature_avg_str = "{:.2f}".format(temp_avg)
        temp_low= (temp_low*1.8) + 32
        temperature_low_str = "{:.2f}".format(temp_low)
        temp_high= (temp_high*1.8) + 32
        temperature_high_str = "{:.2f}".format(temp_high)
        temp_type_str = "F"
        
    if(temp==None): #display error if data not being sent
        ui.label_temp.setText("Error")
    else:
        temperature_str = "{:.2f}".format(temp)
        ui.label_temp.setText(temperature_str) #display temperature
        temperature_avg_str = "{:.2f}".format(temp_avg)
        ui.label_avg_temp.setText(temperature_avg_str) #display temperature
        temperature_low_str = "{:.2f}".format(temp_low)
        ui.label_low_temp.setText(temperature_low_str) #display temperature
        temperature_high_str = "{:.2f}".format(temp_high)
        ui.label_high_temp.setText(temperature_high_str) #display temperature
   
    if(rh==None): #display error if data not being sen
        ui.label_rh.setText("Error")
    else:
        rh_str = "{:.2f}".format(rh) #display humidity
        ui.label_rh.setText(rh_str)
        rh_avg_str = "{:.2f}".format(rh_avg)
        ui.label_avg_rh.setText(rh_avg_str)
        rh_low_str = "{:.2f}".format(rh_low)
        ui.label_low_rh.setText(rh_low_str)
        rh_high_str = "{:.2f}".format(rh_high)
        ui.label_high_rh.setText(rh_high_str)
    
    ui.label_low_temp_timestamp.setText(ts_temp_low) #display timestamps
    ui.label_high_temp_timestamp.setText(ts_temp_high)
    ui.label_low_rh_timestamp.setText(ts_rh_low)
    ui.label_high_rh_timestamp.setText(ts_rh_high)
    
    data_list.append(timestamp) #append measurements to data list
    data_list.append(temperature_str_csv)
    data_list.append(temperature_avg_str_csv)
    data_list.append(rh_str)
    data_list.append(rh_avg_str)
    data_list.append(ts_temp_low)
    data_list.append(temperature_low_str_csv)
    data_list.append(ts_temp_high)
    data_list.append(temperature_high_str_csv)
    data_list.append(ts_rh_low)
    data_list.append(rh_low_str)
    data_list.append(ts_rh_high)
    data_list.append(rh_high_str)
    
    with open('temp_rh_data.csv', 'w') as csvfile: #write data to CSV file
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(data_list)
    print(data_list)
     
def calc_avg():
    """function to calculate averages of temp and rh"""
    temp_sum = 0.0; rh_sum = 0.0;
    for i in range(0,len(time_list)):
        temp_sum += temp_list[i]
        rh_sum += rh_list[i]
    temp_avg = temp_sum/len(time_list)
    rh_avg = rh_sum/len(time_list)
    return temp_avg, rh_avg

def calc_low():
    """function to calculate minimum values of temp and rh"""
    global temp_low, rh_low, ts_temp_low, ts_rh_low
    for i in range(0,len(time_list)):
        if(temp_list[i]<temp_low):
            temp_low = temp_list[i];
            ts_temp_low = time_list[i];
        if(rh_list[i]<rh_low):
            rh_low = rh_list[i];
            ts_rh_low = time_list[i];
    return ts_temp_low, ts_rh_low, temp_low, rh_low

def calc_high():
    """function to calculate maximum values of temp and rh"""
    global temp_high, rh_high, ts_temp_high, ts_rh_high
    for i in range(0,len(time_list)):
        if(temp_list[i]>temp_high):
            temp_high = temp_list[i];
            ts_temp_high = time_list[i];
        if(rh_list[i]>rh_high):
            rh_high = rh_list[i];
            ts_rh_high = time_list[i];
    return ts_temp_high, ts_rh_high, temp_high, rh_high

if __name__ == '__main__':
    main() #call to main function
    