from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class title_elements():
    def __init__(self):
        super().__init__()

        # Title
        self.title = QLabel('To Do List')
        # Set the orientation of widgets
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # Change the default font
        self.title.setFont(QFont("Arial"))

        # Label Title
        self.labelTitle = QLineEdit()
        self.labelTitle.setPlaceholderText("Title")

        self.buttonTitle = QPushButton("Add Title")



class task_elements(QMainWindow):
    def __init__(self):
        super().__init__()

        # Line edit for task
        self.labelTask = QLineEdit()
        self.checkBoxTask = QCheckBox()
        self.deleteTaskButton = QPushButton("X")

        self.add_task_layout = QHBoxLayout()
        self.add_task_layout.addWidget(self.checkBoxTask)  # , alignment=Qt.AlignLeft | Qt.AlignTop)
        self.add_task_layout.addWidget(self.labelTask)  # , alignment=Qt.AlignLeft | Qt.AlignTop)
        self.add_task_layout.addWidget(self.deleteTaskButton)

        #self.checkBoxTask.stateChanged.connect(self.deleteLater)
        #self.deleteTaskButton.clicked.connect(self.deleteLater)
        self.deleteTaskButton.clicked.connect(self.fun1)

    def fun1(self):
        self.deleteTaskButton.clicked.connect(self.add_task_layout.deleteLater)
        print('delete')