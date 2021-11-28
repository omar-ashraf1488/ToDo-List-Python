from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLCDNumber, QPushButton, QLabel, QComboBox, QVBoxLayout
from PyQt5.QtCore import QTimer

class Timer(QWidget):
    def __init__(self):
        super().__init__()

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

        self.comboBox.activated.connect(self.selectWorkDuration)

    def selectWorkDuration(self):
        self.text = self.comboBox.currentText()
        self.lcd.display(self.text)

