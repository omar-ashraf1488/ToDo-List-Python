from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

        # The windows name
        self.setWindowTitle("To do List")

        self.setGeometry(0, 0, self.width, self.height)

        # The Title
        self.title = QLabel('To Do List')
        self.title.setStyleSheet(
            'font-size:{0}px; font-weight:bold; text-align: center; color:black; border-style:none;'.format(
                int(height / 12)))
        # Set the orientation of widgets
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # Change the default font
        self.title.setFont(QFont("Arial"))

        # Label Title
        self.labelTitle = QLineEdit()
        self.labelTitle.setPlaceholderText("Title")
        ###########################################
        self.buttonTitle = QPushButton("Add Title")
        ###########################################
        self.buttonAddTask = QPushButton("+")
        self.buttonAddTask.setFixedSize(int(width / 20), int(height / 25))

        # Actions of Buttons
        self.buttonTitle.clicked.connect(self.addTitle)
        self.buttonAddTask.clicked.connect(self.addTask)

        self.initUI(self.width, self.height)  # Initialize the UI

    def initUI(self, width, height):
        # Horizontal box layout objects
        self.lineEditButtonlayout = QHBoxLayout()
        self.lineEditButtonlayout.addWidget(self.labelTitle)
        self.lineEditButtonlayout.addWidget(self.buttonTitle)

        self.lineEditButtonWidget = QWidget()
        # set layout of window frame is lineEditButtonlayout
        self.lineEditButtonWidget.setLayout(self.lineEditButtonlayout)

        self.addTaskButtonlayout = QHBoxLayout()
        self.addTaskButtonlayout.addWidget(self.buttonAddTask, alignment=Qt.AlignLeft | Qt.AlignTop)

        self.addTaskButtonWidget = QWidget()
        # set layout of window frame is lineEditButtonlayout
        self.addTaskButtonWidget.setLayout(self.addTaskButtonlayout)



        # vertical box layout objects
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.title)
        self.mainlayout.addWidget(self.lineEditButtonWidget)
        self.mainlayout.addWidget(self.addTaskButtonWidget)


        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainlayout)
        # center the widget of frame
        self.setCentralWidget(self.mainWidget)

    # Actions of buttons functions
    def addTitle(self):
        self.buttonTitle.setText("Change the Title")

    def addTask(self):
        self.buttonAddTask.setText("-")
        print("add task")
        #self.Task = QLineEdit()
        if self.buttonAddTask.clicked():
            self.updateAddtask()


    def updateAddtask(self):
        print("clicked")
            #self.buttonAddTask.setText("+")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    V = app.desktop().screenGeometry()
    width = V.width()
    height = V.height()

    main = MainWindow(500, 800)
    main.show()

    sys.exit(app.exec())
