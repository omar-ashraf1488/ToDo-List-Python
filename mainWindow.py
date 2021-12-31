from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
import os


from db.create_db import create_db
from tabsController import TabsController


class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

        self.setWindowIcon(QIcon('Images/logo.png'))
        self.setWindowTitle("To do List")
        self.setFixedSize(self.width, self.height)
        self.setGeometry(100, 100, self.width, self.height)
        self.setStyleSheet("font-family: Arial, Helvetica, sans-serif;")

        self.title = QLabel('To Do List')
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title.setStyleSheet(
            'font-size:{0}px; font-weight:bold; color:black;'.format(
                int(height / 12)))

        self.tabs = TabsController()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.title)
        self.mainLayout.addWidget(self.tabs)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    if not os.path.exists("to_do.db"):
        create_db("to_do.db")
        new_db = QMessageBox()
        new_db.setWindowTitle("New Database")
        new_db.setText("New database created")
        new_db.exec_()


    main = MainWindow(500, 800)
    main.show()

    sys.exit(app.exec())