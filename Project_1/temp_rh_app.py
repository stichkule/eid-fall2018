# -*- coding: utf-8 -*-
"""
Python code to implement the temperature and relative humidity monitoring application for Project 1 of ECEN 5053.
The GUI for this app was created using Qt Designer and can be found in the file temp_rh_dashboard.ui. This app
interfaces with the GUI using the converted file temp_rh_dashboard.py. Temperature and relative humidity measurements
are made using a DHT22 sensor connected to the Raspberry Pi. The app includes the following functionality:
* Temperature reading in deg C and F
* Configurable periodic interval for fetching sensor data
* Setting thresholds for temperature and relative humidity alarms
* Plotting time series of fetched data
* Login screen to secure the application

Running the App: issue the command -- sudo python3 temp_rh_app.py from a Bash shell

@author: Shiril Tichkule
@date: 30 September 2018
"""

import sys
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
update_interval = 60 # refresh interval in seconds
unit = 'C' #default temperature units
temp_alarm_threshold=0 #default temperature threshold
rh_alarm_threshold=0 #default RH threshold
temp_list=[] #lists for storing temp, rh, and timestamp data for plotting
rh_list=[]
time_list=[]
fmtr = dates.DateFormatter("%H:%M:%S") #date format for timestamp display

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
        ui.pushButton_REFRESH.clicked.connect(lambda:update_data()) #update data if refresh button clicked
        ui.radioButton_F.clicked.connect(lambda:change_to_F()) #change units of temperature display
        ui.radioButton_C.clicked.connect(lambda:change_to_degC())
        ui.pushButton_OK.clicked.connect(lambda:update_refresh_interval()) #change periodic refresh interval
        ui.pushButton_PLOT.clicked.connect(lambda:plot_data()) #plot sensor data

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
    #function to update temperature, humidity and alarms on display 
    global temperature, humidity, unit, ui
    
    t = threading.Timer(update_interval,update_data).start() # thread to autorun function once every update interval
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) #read sensor data
    timestamp=datetime.now().strftime('%d %b %Y %H:%M:%S') #format timestamp
    ui.label_timestamp.setText(timestamp)
    
    temp_list.append(temperature) #append data to lists for plotting
    rh_list.append(humidity)
    time_list.append(datetime.strptime(timestamp,'%d %b %Y %H:%M:%S'))
    
    if(unit=='F' and temperature!=None): # if unit is set to F, convert from deg C to F
        temperature= (temperature*1.8) + 32
        temperature_str = "{:.2f}".format(temperature) 
    
    if(temperature==None): #display error if data not being sent
        ui.label_temp.setText("Error")
    else:
        temperature_str = "{:.2f}".format(temperature)
        ui.label_temp.setText(temperature_str) #display temperature
   
    if(humidity==None): #display error if data not being sen
        ui.label_rh.setText("Error")
    else:
        rh_str = "{:.2f}".format(humidity)
        ui.label_rh.setText(rh_str)
    if(ui.checkBox_yes.isChecked()): #check if alarms are ON
        alarm_check()
    else:
        temp_alarm_off()
        rh_alarm_off()
   
def read_threshold():
    """function to read alarm thresholds"""
    global temp_alarm_threshold, rh_alarm_threshold
    temp_alarm_threshold=int(ui.label_temp_dial.text()) #read and set thresholds
    rh_alarm_threshold=int(ui.label_rh_dial.text())
    
def alarm_check(): 
    """function to check if alarms need to be activated"""
    read_threshold()
    global temp_alarm_threshold, rh_alarm_threshold, unit
    global temperature,humidity
    if((unit=='F' and int(temperature)>int((temp_alarm_threshold*1.8)+32) #check and activate alarms
    or (unit=='C' and int(temperature)>temp_alarm_threshold))):
        temp_alarm_on()
    elif((unit=='F' and int(temperature)<int((temp_alarm_threshold*1.8)+32) 
    or (unit=='C' and int(temperature)<temp_alarm_threshold))):
        temp_alarm_off()
        
    if(int(humidity)>rh_alarm_threshold):
        rh_alarm_on()
    else: rh_alarm_off()
 
def temp_alarm_on():
    """Turn on temperarutre alarm by displaying red LCD"""
    ui.lcd_temp.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
    
def temp_alarm_off():
    """Turn off temperarutre alarm by displaying green LCD"""
    ui.lcd_temp.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 255, 0);\n"
"}")
    
def rh_alarm_on():
    """Turn on relative humidity alarm by displaying red LCD"""
    ui.lcd_rh.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
    
def rh_alarm_off():
    """Turn off relative humidity alarm by displaying green LCD"""
    ui.lcd_rh.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 255, 0);\n"
"}")
    
def plot_data():
    """function to plot temperature and relative humidity time series"""
    fig = plt.figure()
    fig.suptitle('Temperature and Relative Humidity time series')
    plt.subplot(2,1,1) #temperature plot
    plt.plot(time_list,temp_list)
    ax=plt.gca()
    ax.xaxis.set_major_formatter(fmtr) #format x axis to display formatted time
    plt.xlabel('Time [hh:mm:ss]')
    plt.ylabel('Temperature [deg C]')
    
    plt.subplot(2,1,2) #relative humidity plot
    plt.plot(time_list,rh_list)
    ax=plt.gca()
    ax.xaxis.set_major_formatter(fmtr)
    plt.xlabel('Time [hh:mm:ss]')
    plt.ylabel('Relative Humidity [%]')
    
    plt.show()
    
if __name__ == '__main__':
    main() #call to main function