from task import *
import sys



class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.index_list = []

        # The windows name
        self.setWindowTitle("To do List")

        self.setGeometry(0, 0, self.width, self.height)

        task_object = task_elements()
        title_object = title_elements()

        # The Title
        self.title = title_object.title
        self.title.setStyleSheet(
            'font-size:{0}px; font-weight:bold; text-align: center; color:black; border-style:none;'.format(
                int(height / 12)))

        # Label Title
        self.labelTitle = title_object.labelTitle
        self.buttonTitle = title_object.buttonTitle


        # Line edit for task
        self.deleteTaskButton = task_object.deleteTaskButton
        self.deleteTaskButton.setFixedSize(int(width / 20), int(height / 25))


        self.buttonAddTask = QPushButton("+")
        self.buttonAddTask.setFixedSize(int(width / 20), int(height / 25))
        self.text = QLabel('ِAdd task')

        # Actions of Buttons
        self.buttonTitle.clicked.connect(self.addTitle)
        self.buttonAddTask.clicked.connect(self.addTask)
        self.deleteTaskButton.clicked.connect(self.deleteTask)
        # Actions of checkbox
        #self.checkBoxTask.stateChanged.connect(lambda: self.checkBoxtaskChecked(self.checkBoxTask, self.labelTask))

        self.initUI(self.width, self.height)  # Initialize the UI

    def initUI(self, width, height):
        task_object = task_elements()

        # Horizontal box layout objects
        self.lineEditButtonlayout = QHBoxLayout()
        self.lineEditButtonlayout.addWidget(self.labelTitle)
        self.lineEditButtonlayout.addWidget(self.buttonTitle)

        self.lineEditButtonWidget = QWidget()
        # set layout of window frame is lineEditButtonlayout
        self.lineEditButtonWidget.setLayout(self.lineEditButtonlayout)

        # Task layout
        self.add_task_layout = task_object.add_task_layout
        # Task widget
        self.add_task_widget = QWidget()
        self.add_task_widget.setLayout(self.add_task_layout)

        # scroll area widget contents - layout
        self.tasks_layout = QFormLayout()

        # scroll area widget contents
        self.tasks_widget = QWidget()
        self.tasks_widget.setLayout(self.tasks_layout)

        # scroll area
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.tasks_widget)


        self.addTasklayout2 = QHBoxLayout()
        self.addTasklayout2.addWidget(self.buttonAddTask, alignment=Qt.AlignLeft)
        self.addTasklayout2.addWidget(self.text, alignment=Qt.AlignLeft)

        self.addTask2Widget = QWidget()
        # set layout of window frame is lineEditButtonlayout
        self.addTask2Widget.setLayout(self.addTasklayout2)

        # vertical box layout objects
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.title)
        self.mainlayout.addWidget(self.lineEditButtonWidget)
        #self.mainlayout.addWidget(self.add_tasks_widget)
        self.mainlayout.addWidget(self.scrollArea)
        self.mainlayout.addWidget(self.addTask2Widget)




        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainlayout)
        # center the widget of frame
        self.setCentralWidget(self.mainWidget)

    # Actions of buttons functions
    def addTitle(self):
        self.buttonTitle.setText("Change the Title")

    def addTask(self):
        print("add")
        task = task_elements()
        self.index_list.append(task)
        self.tasks_layout.addRow(task.add_task_layout)
        # self.tasks_layout.removeRow(task_elements().deleteLater())

        #self.add_tasklayout.insertWidget(0, self.checkBoxTask)
        #self.buttonAddTask.clicked.disconnect()
        #self.buttonAddTask.setText("-")
        #self.buttonAddTask.clicked.connect(self.updateAddtask)

    def deleteTask(self):
        pass

    # Actions of checkbox functions
    def checkBoxtaskChecked(self, checkBox, lineEdit):
        if checkBox.isChecked():
            lineEdit.setDisabled(True)
        else:
            lineEdit.setDisabled(False)




    def updateAddtask(self):
        self.buttonAddTask.clicked.disconnect()
        self.buttonAddTask.setText("+")
        self.buttonAddTask.clicked.connect(self.addTask)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    V = app.desktop().screenGeometry()
    width = V.width()
    height = V.height()

    main = MainWindow(500, 800)
    main.show()

    sys.exit(app.exec())
