# -*- coding: utf-8 -*-
"""
Python code to implement the temperature and relative humidity monitoring application for Client for Project 3 of ECEN
5053. The GUI for this app was created using Qt Designer and can be found in the file temp_rh_dashboard.ui. This app
interfaces with the GUI using the converted file temp_rh_dashboard.py. Temperature and relative humidity measurements
are made using a DHT22 sensor connected to the Raspberry Pi on server side. The measured data and timestamps are written
on to AWS Simple Queue Service. This application receives messages from the queue.
The app includes the following functionality:
* Read Temperature and RH values from the queue and delete them
* CDisplay Temperature in selected unit on the UI
* Display of temperature and humidity statistics (low, high, average values) and plots
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
import boto3
import ast

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

sqs = boto3.resource('sqs') #initialize sqs resource
queue = sqs.get_queue_by_name(QueueName='RPi3-FIFO.fifo') #intantiate queue to recieve messages

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
        #update_data() #update data at periodic interval
        ui.radioButton_F.clicked.connect(lambda:change_to_F()) #change units of temperature display
        ui.radioButton_C.clicked.connect(lambda:change_to_degC())
        ui.pushButton_Fetch.clicked.connect(lambda:fetch_and_plot())

def main():
    """main function that invokes controller class methods"""
    app = QApplication(sys.argv) #launch app
    controller = Controller() #launch controller
    controller.show_login() #show login window
    sys.exit(app.exec_()) #exit app
    
def fetch_and_plot():
    """
    Fetch 30 data items from sqs ques using boto3
    Get latest data and update UI
    plot values for humidity and temp
    """
    
    global temp, temp_low, temp_high, temp_avg, rh, rh_low, rh_high, rh_avg, ts_temp_low, ts_temp_high, ts_rh_low, ts_rh_high, unit, ui, cntr;
    global queue
    
    #lists for plotting data
    temp_list = []
    temp_high_list = []
    temp_low_list = []
    temp_avg_list = []
    rh_list = []
    rh_high_list = []
    rh_low_list = []
    rh_avg_list = []
    ts_list = []
    count = 0 #To check if queue is not empty
    
    #Loop to receive 30 messgaes and append data to the lists for plotting
    for i in range(3):
        response = queue.receive_messages(QueueUrl='https://sqs.us-west-2.amazonaws.com/572594505086/RPi3-FIFO.fifo',MaxNumberOfMessages=10)
        for msg in response:
            count = count + 1
            m = ast.literal_eval(msg.body)
            temp_list.append(float(m['temperature_str']))
            temp_high_list.append(float(m['temperature_high_str']))
            temp_low_list.append(float(m['temperature_low_str']))
            temp_avg_list.append(float(m['temperature_avg_str']))
            rh_list.append(float(m['rh_str']))
            rh_high_list.append(float(m['rh_high_str']))
            rh_low_list.append(float(m['rh_low_str']))
            rh_avg_list.append(float(m['rh_avg_str']))
            ts_list.append(datetime.strptime(m['timestamp'],'%d %b %Y %H:%M:%S'))
            msg.delete()
            
    # queue was empty
    if count == 0:
        print('Empty Queue')
        return

    #Set Humdity Labels
    ui.label_rh.setText(m['rh_str'])
    ui.label_avg_rh.setText(m['rh_avg_str'])
    ui.label_low_rh.setText(m['rh_low_str'])
    ui.label_high_rh.setText(m['rh_high_str'])
    
    #Values for temperature - Always in Celcius
    temp = float(m['temperature_str'])
    temp_avg = float(m['temperature_avg_str'])
    temp_low = float(m['temperature_low_str'])
    temp_high = float(m['temperature_high_str'])
    
    #update temperature data in UI
    update_data()
    
    #Set  timestamp labels
    ui.label_low_temp_timestamp.setText(m['ts_temp_low']) #display timestamps
    ui.label_high_temp_timestamp.setText(m['ts_temp_high'])
    ui.label_low_rh_timestamp.setText(m['ts_rh_low'])
    ui.label_high_rh_timestamp.setText(m['ts_rh_high'])
    ui.label_timestamp.setText(m['timestamp'])
    
    #For plotting temperature and relative humidity time series
    fig = plt.figure()
    fig.suptitle('Temperature and Relative Humidity Values fetched = ' + str(count))
    plt.subplot(2,1,1) #temperature plot
    plt.plot(ts_list,temp_list)
    plt.plot(ts_list,temp_high_list)
    plt.plot(ts_list,temp_low_list)
    plt.plot(ts_list,temp_avg_list)
    plt.legend(['Curr','Max','Min','Avg'],loc='upper left')
    ax=plt.gca()
    ax.xaxis.set_major_formatter(fmtr) #format x axis to display formatted time
    plt.xlabel('Time [hh:mm:ss]')
    plt.ylabel('Temperature [deg C]')
    
    plt.subplot(2,1,2) #relative humidity plot
    plt.plot(ts_list,rh_list)
    plt.plot(ts_list,rh_high_list)
    plt.plot(ts_list,rh_low_list)
    plt.plot(ts_list,rh_avg_list)
    plt.legend(['Curr','Max','Min','Avg'],loc='upper left')
    ax=plt.gca()
    ax.xaxis.set_major_formatter(fmtr)
    plt.xlabel('Time [hh:mm:ss]')
    plt.ylabel('Relative Humidity [%]')
    
    plt.show()

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

def update_data():
    
    """function to update temperature, humidity depending on radio button selected"""
    
    global temp, temp_low, temp_high, temp_avg, rh, rh_low, rh_high, rh_avg, ts_temp_low, ts_temp_high, ts_rh_low, ts_rh_high, unit, ui, cntr;
    
    if(unit=='F'): # if unit is set to F, convert from deg C to F
        temp_f= (temp*1.8) + 32
        temperature_str_f = "{:.2f}".format(temp_f)
        temp_avg_f= (temp_avg*1.8) + 32
        temperature_avg_str_f = "{:.2f}".format(temp_avg_f)
        temp_low_f= (temp_low*1.8) + 32
        temperature_low_str_f = "{:.2f}".format(temp_low_f)
        temp_high_f= (temp_high*1.8) + 32
        temperature_high_str_f = "{:.2f}".format(temp_high_f)
        ui.label_temp.setText(temperature_str_f) #display temperature
        ui.label_avg_temp.setText(temperature_avg_str_f) #display temperature
        ui.label_low_temp.setText(temperature_low_str_f) #display temperature
        ui.label_high_temp.setText(temperature_high_str_f) #display temperature
    else:    
        temperature_str = "{:.2f}".format(temp)
        ui.label_temp.setText(temperature_str) #display temperature
        temperature_avg_str = "{:.2f}".format(temp_avg)
        ui.label_avg_temp.setText(temperature_avg_str) #display temperature
        temperature_low_str = "{:.2f}".format(temp_low)
        ui.label_low_temp.setText(temperature_low_str) #display temperature
        temperature_high_str = "{:.2f}".format(temp_high)
        ui.label_high_temp.setText(temperature_high_str) #display temperature

if __name__ == '__main__':
    main() #call to main function
    