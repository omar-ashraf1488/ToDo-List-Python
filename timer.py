from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLCDNumber, QPushButton, QLabel, QComboBox, QVBoxLayout
from PyQt5.QtCore import QTimer

class Timer(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer()

        self.label = QLabel("Work Duration in Minutes")
        self.comboBox = QComboBox()
        self.comBoxItems = self.comboBox.addItems(["05:00", "10:00", "15:00", "20:00", "25:00", "30:00"])

        self.lcd = QLCDNumber()
        self.text = self.comboBox.currentText()
        self.lcd.display(self.text)
        self.startButton = QPushButton("Start")
        self.stopButton = QPushButton("Stop")
        self.resetButton = QPushButton("Reset")

        self.timerInputLayout = QHBoxLayout()
        self.timerInputLayout.addWidget(self.label)
        self.timerInputLayout.addWidget(self.comboBox)
        self.timerInputWidget = QWidget()
        self.timerInputWidget.setLayout(self.timerInputLayout)

        self.timerLayout = QHBoxLayout()
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

    def selectWorkDuration(self):
        self.timerString = self.comboBox.currentText()
        self.lcd.display(self.timerString)
        self.time = self.stringTimeToInt(self.timerString)

    def stringTimeToInt(self, timerString):
        mm, ss = map(int, timerString.split(':'))
        return ss + 60 * mm

    def startTimer(self):
        self.startButton.setEnabled(False)
        self.timer.timeout.connect(self.timerTimeout)
        self.time = self.stringTimeToInt(self.timerString)
        self.timer.start(self.time)

    def timerTimeout(self):
        self.time -= 1
        if self.time == 0:
            self.time = self.durationTime
        self.updateLCD()

    def updateLCD(self):
        m, s = divmod(self.time, 60)
        self.lcd.display('{:0>2}:{:0>2}'.format(m, s))

    def stopTimer(self):
        self.startButton.setEnabled(True)
        self.timer.stop()
