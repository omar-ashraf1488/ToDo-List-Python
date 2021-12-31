from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLCDNumber, QPushButton, QLabel, QComboBox, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from css import PushButtonStyle, LCDStyle

class Timer(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer()

        self.label = QLabel("Work Duration in Minutes")
        self.comboBox = QComboBox()
        self.comBoxItems = self.comboBox.addItems(["05:00", "10:00", "15:00", "20:00", "25:00", "30:00"])

        self.lcd = QLCDNumber()
        self.lcd.setFixedSize(100,50)
        self.lcd.setSegmentStyle(2)

        self.text = self.comboBox.currentText()
        self.lcd.display(self.text)
        self.startButton = QPushButton("Start")
        self.stopButton = QPushButton("Stop")
        self.resetButton = QPushButton("Reset")

        self.startButton.setStyleSheet(PushButtonStyle)
        self.stopButton.setStyleSheet(PushButtonStyle)
        self.resetButton.setStyleSheet(PushButtonStyle)
        self.startButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.resetButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.timerInputLayout = QHBoxLayout()
        self.timerInputLayout.addWidget(self.label)
        self.timerInputLayout.addWidget(self.comboBox)
        self.timerInputWidget = QWidget()
        self.timerInputWidget.setLayout(self.timerInputLayout)

        self.timerLayout = QHBoxLayout()
        #self.timerLayout.setSpacing(0)
        self.timerLayout.addWidget(self.lcd)
        self.timerLayout.addWidget(self.startButton)
        self.timerLayout.addWidget(self.stopButton)
        self.timerLayout.addWidget(self.resetButton)
        self.timerWidget = QWidget()
        self.timerWidget.setLayout(self.timerLayout)


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.timerInputWidget)
        self.mainLayout.addWidget(self.timerWidget)

        self.setLayout(self.mainLayout)

        self.selectWorkDuration()
        self.comboBox.activated.connect(self.selectWorkDuration)
        self.startButton.clicked.connect(self.startTimer)
        self.stopButton.clicked.connect(self.stopTimer)
        self.resetButton.clicked.connect(self.resetTimer)

    def selectWorkDuration(self):
        global time
        self.timeString = self.comboBox.currentText()
        self.lcd.display(self.timeString)
        self.lcd.setStyleSheet(LCDStyle)

        time = self.stringTimeToInt(self.timeString)

    def stringTimeToInt(self, timerString):
        mm, ss = map(int, timerString.split(':'))
        return ss + 60 * mm

    def startTimer(self):
        global time
        self.timer.start(1000)  # fires every 1000ms = 1s
        if time > 0:
            self.startButton.setEnabled(False)
            self.resetButton.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.timer.timeout.connect(self.timerTimeout)
        else:
            QMessageBox.warning(self, "Warning!", "You must select Work Duration!")

    def timerTimeout(self):
        global time
        time -= 1

        if time <= 0:
            self.stopTimer()
            self.lcd.display('00:00')
        else:
            self.updateLCD()

        if time <= 120:
            self.lcd.setStyleSheet("color: red ; background-color: rgb(0,100,0)")

    def updateLCD(self):
        global time
        m, s = divmod(time, 60)
        self.lcd.display('{:0>2}:{:0>2}'.format(m, s))

    def stopTimer(self):
        self.startButton.setEnabled(True)
        self.resetButton.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.timer.stop()

    def resetTimer(self):
        self.timer.stop()
        self.startButton.setEnabled(True)
        self.selectWorkDuration()

