from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLCDNumber, QPushButton
from PyQt5.QtCore import QTimer

class Timer(QWidget):
    def __init__(self):
        super().__init__()

        self.lcd = QLCDNumber()
        self.lcd.display("30:00")
        self.startButton = QPushButton("Start")
        self.stopButton = QPushButton("Stop")
        self.resetButton = QPushButton("Reset")

        self.timerLayout = QHBoxLayout()
        self.timerLayout.addWidget(self.lcd)
        self.timerLayout.addWidget(self.startButton)
        self.timerLayout.addWidget(self.stopButton)
        self.timerLayout.addWidget(self.resetButton)

        self.setLayout(self.timerLayout)
        

