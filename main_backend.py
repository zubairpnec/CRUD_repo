import time

from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QMainWindow
from main_front import *  # <-- Add file name
from create_backend import *
from auth_back import *


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() # <-- Add window name here
        self.ui.setupUi(self)
        #‘’’Add your code here’’’
        self.setWindowTitle('Employee Management System')
        self.auth_form = None
        self.ui.create_btn.clicked.connect(self.create_def)
        self.ui.read_btn.clicked.connect(self.read_def)
        self.ui.update_btn.clicked.connect(self.update_def)
        self.ui.delete_btn.clicked.connect(self.delete_def)
        self.ui.exit_btn.clicked.connect(self.exit_def)

    def create_def(self):
        self.auth_form = auth_form_class("create")
        self.auth_form.show()

    def read_def(self):
        self.auth_form = auth_form_class("read")
        self.auth_form.show()

    def update_def(self):
        self.auth_form = auth_form_class("update")
        self.auth_form.show()

    def delete_def(self):
        self.auth_form = auth_form_class("delete")
        self.auth_form.show()

    def exit_def(self):
        self.close()




if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Qt Modern')
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
