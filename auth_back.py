import sys
from PyQt5.QtWidgets import QApplication,QDialog
from auth_front import *  # <-- Add file name
from create_backend import *
from read_backend import *
from update_backend import *
from delete_backend import *

class auth_form_class(QDialog):
    def __init__(self, action_idx):
        super().__init__()
        self.ui = Ui_auth() # <-- Add window name here
        self.ui.setupUi(self)
        #‘’’Add your code here’’’
        self.setWindowTitle('Password Manager')
        self.username = "admin"
        self.password = "admin"
        self.next_form = None
        self.ui.ok_btn.clicked.connect(self.ok_def)
        self.ui.cancel_btn.clicked.connect(self.cancel_def)
        self.action_idx = action_idx
        self.ui.name_txt.setText("admin")
        self.ui.pw_txt.setText("admin")

    def ok_def(self):
        if self.ui.name_txt.text() == self.username:
            if self.ui.pw_txt.text() == self.password:
                if self.action_idx == "create":
                    self.next_form = create_form_class()
                    self.next_form.show()
                    self.close()
                if self.action_idx == "read":
                    self.next_form = read_form_class()
                    self.next_form.show()
                    self.close()
                if self.action_idx == "update":
                    self.next_form = update_form_class()
                    self.next_form.show()
                    self.close()
                if self.action_idx == "delete":
                    self.next_form = delete_form_class()
                    self.next_form.show()
                    self.close()
            else:
                self.incorrect()
        else:
            self.incorrect()

    def cancel_def(self):
        self.close()

    def incorrect(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText('Information !')
        msg.setInformativeText('incorrect username or password')
        msg.setWindowTitle('Message Box')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()




if __name__=="__main__":
    app = QApplication(sys.argv)
    w = auth_form_class("abc")
    w.show()
    sys.exit(app.exec_())
