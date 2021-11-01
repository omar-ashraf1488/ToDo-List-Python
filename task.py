from PyQt5.QtWidgets import *

#from window_GUI import main_window

# Import threading to avoid crashing the app
import cgitb
cgitb.enable(format='text')


class TaskElements(QMainWindow):
    def __init__(self, description, height, width, task_id=None, removeTask=None):
        self.description = description
        self.removeTask = removeTask
        self.task_id = task_id
        self.height = height
        self.width = width
        super().__init__()


        # Line edit for task
        self.labelTask = QLineEdit()
        self.checkBoxTask = QCheckBox()
        self.deleteTaskButton = QPushButton("X")
        self.deleteTaskButton.setFixedSize(int(self.width / 20), int(self.height / 25))


        self.taskLayout = QHBoxLayout()
        self.taskLayout.addWidget(self.labelTask)
        self.taskLayout.addWidget(self.deleteTaskButton)

        self.labelTask.setText(self.description)


        # Action of Delete Button
        self.deleteTaskButton.clicked.connect(self.delete_task)


    # Delete task function
    def delete_task(self):
        print("delete")
        self.removeTask(self.task_id)
        #main_window.index_list.pop().deletlater()
        # MainWindow().index_list.pop.deletelater()
