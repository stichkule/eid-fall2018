# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp_rh_dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 160, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 160, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 60, 341, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 90, 741, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 220, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 250, 141, 21))
        self.label_5.setObjectName("label_5")
        self.radioButton_C = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_C.setGeometry(QtCore.QRect(590, 280, 71, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_C.setFont(font)
        self.radioButton_C.setChecked(True)
        self.radioButton_C.setObjectName("radioButton_C")
        self.radioButton_F = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_F.setGeometry(QtCore.QRect(700, 280, 41, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_F.setFont(font)
        self.radioButton_F.setObjectName("radioButton_F")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 290, 211, 21))
        self.label_6.setObjectName("label_6")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(590, 320, 171, 21))
        self.label_17.setObjectName("label_17")
        self.text_refresh = QtWidgets.QTextEdit(self.centralwidget)
        self.text_refresh.setGeometry(QtCore.QRect(590, 350, 104, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_refresh.sizePolicy().hasHeightForWidth())
        self.text_refresh.setSizePolicy(sizePolicy)
        self.text_refresh.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_refresh.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_refresh.setObjectName("text_refresh")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(700, 360, 91, 21))
        self.label_18.setObjectName("label_18")
        self.pushButton_OK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OK.setGeometry(QtCore.QRect(640, 390, 51, 31))
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(220, 220, 67, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_temp.setFont(font)
        self.label_temp.setObjectName("label_temp")
        self.label_rh = QtWidgets.QLabel(self.centralwidget)
        self.label_rh.setGeometry(QtCore.QRect(390, 220, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rh.setFont(font)
        self.label_rh.setObjectName("label_rh")
        self.label_timestamp = QtWidgets.QLabel(self.centralwidget)
        self.label_timestamp.setGeometry(QtCore.QRect(280, 290, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_timestamp.setFont(font)
        self.label_timestamp.setObjectName("label_timestamp")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 220, 91, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 350, 91, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 440, 91, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 250, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_low_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_low_temp.setGeometry(QtCore.QRect(220, 350, 67, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_low_temp.setFont(font)
        self.label_low_temp.setObjectName("label_low_temp")
        self.label_high_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_high_temp.setGeometry(QtCore.QRect(220, 440, 67, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_high_temp.setFont(font)
        self.label_high_temp.setObjectName("label_high_temp")
        self.label_avg_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_avg_temp.setGeometry(QtCore.QRect(220, 250, 67, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_avg_temp.setFont(font)
        self.label_avg_temp.setObjectName("label_avg_temp")
        self.label_low_rh = QtWidgets.QLabel(self.centralwidget)
        self.label_low_rh.setGeometry(QtCore.QRect(390, 350, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_low_rh.setFont(font)
        self.label_low_rh.setObjectName("label_low_rh")
        self.label_high_rh = QtWidgets.QLabel(self.centralwidget)
        self.label_high_rh.setGeometry(QtCore.QRect(390, 440, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_high_rh.setFont(font)
        self.label_high_rh.setObjectName("label_high_rh")
        self.label_avg_rh = QtWidgets.QLabel(self.centralwidget)
        self.label_avg_rh.setGeometry(QtCore.QRect(390, 250, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_avg_rh.setFont(font)
        self.label_avg_rh.setObjectName("label_avg_rh")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(450, 350, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(450, 440, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(450, 250, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 380, 161, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 470, 161, 21))
        self.label_15.setObjectName("label_15")
        self.label_low_temp_timestamp = QtWidgets.QLabel(self.centralwidget)
        self.label_low_temp_timestamp.setGeometry(QtCore.QRect(220, 380, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_low_temp_timestamp.setFont(font)
        self.label_low_temp_timestamp.setObjectName("label_low_temp_timestamp")
        self.label_low_rh_timestamp = QtWidgets.QLabel(self.centralwidget)
        self.label_low_rh_timestamp.setGeometry(QtCore.QRect(390, 380, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_low_rh_timestamp.setFont(font)
        self.label_low_rh_timestamp.setObjectName("label_low_rh_timestamp")
        self.label_high_temp_timestamp = QtWidgets.QLabel(self.centralwidget)
        self.label_high_temp_timestamp.setGeometry(QtCore.QRect(220, 470, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_high_temp_timestamp.setFont(font)
        self.label_high_temp_timestamp.setObjectName("label_high_temp_timestamp")
        self.label_high_rh_timestamp = QtWidgets.QLabel(self.centralwidget)
        self.label_high_rh_timestamp.setGeometry(QtCore.QRect(390, 470, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_high_rh_timestamp.setFont(font)
        self.label_high_rh_timestamp.setObjectName("label_high_rh_timestamp")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ECEN_5053 -- Project_3 -- Temp/RH webserver"))
        self.label.setText(_translate("MainWindow", "Temperature"))
        self.label_2.setText(_translate("MainWindow", "Relative Humidity"))
        self.label_3.setText(_translate("MainWindow", "Temperature and Relative Humidity values "))
        self.label_4.setText(_translate("MainWindow", "%"))
        self.label_5.setText(_translate("MainWindow", "Select display units"))
        self.radioButton_C.setText(_translate("MainWindow", "deg C"))
        self.radioButton_F.setText(_translate("MainWindow", "F"))
        self.label_6.setText(_translate("MainWindow", "Most Recent Data Fetched at"))
        self.label_17.setText(_translate("MainWindow", "Set auto-refresh interval "))
        self.text_refresh.setPlaceholderText(_translate("MainWindow", "5"))
        self.label_18.setText(_translate("MainWindow", "seconds"))
        self.pushButton_OK.setText(_translate("MainWindow", "OK"))
        self.label_temp.setText(_translate("MainWindow", "N/A"))
        self.label_rh.setText(_translate("MainWindow", "N/A"))
        self.label_timestamp.setText(_translate("MainWindow", "N/A"))
        self.label_7.setText(_translate("MainWindow", "Current"))
        self.label_8.setText(_translate("MainWindow", "Lowest"))
        self.label_9.setText(_translate("MainWindow", "Highest"))
        self.label_10.setText(_translate("MainWindow", "Average"))
        self.label_low_temp.setText(_translate("MainWindow", "N/A"))
        self.label_high_temp.setText(_translate("MainWindow", "N/A"))
        self.label_avg_temp.setText(_translate("MainWindow", "N/A"))
        self.label_low_rh.setText(_translate("MainWindow", "N/A"))
        self.label_high_rh.setText(_translate("MainWindow", "N/A"))
        self.label_avg_rh.setText(_translate("MainWindow", "N/A"))
        self.label_11.setText(_translate("MainWindow", "%"))
        self.label_12.setText(_translate("MainWindow", "%"))
        self.label_13.setText(_translate("MainWindow", "%"))
        self.label_14.setText(_translate("MainWindow", "Timestamp @ Lowest"))
        self.label_15.setText(_translate("MainWindow", "Timestamp @ Highest"))
        self.label_low_temp_timestamp.setText(_translate("MainWindow", "N/A"))
        self.label_low_rh_timestamp.setText(_translate("MainWindow", "N/A"))
        self.label_high_temp_timestamp.setText(_translate("MainWindow", "N/A"))
        self.label_high_rh_timestamp.setText(_translate("MainWindow", "N/A"))

