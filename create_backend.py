import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog
from create_front import *  # <-- Add file name
import sqlite3
import numpy as num
class create_form_class(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog() # <-- Add window name here
        self.ui.setupUi(self)
        #‘’’Add your code here’’’
        self.setWindowTitle('CREATE RECORD')
        self.ui.comboBox.hide()
        self.ui.comboBox_label.hide()
        self.ui.open_record.hide()
        self.ui.del_record.hide()
        self.ui.save_btn.clicked.connect(self.save_file_def)
        self.ui.exit_btn.clicked.connect(self.exit_func)
        self.ui.pic_btn.clicked.connect(self.pic_def)
        self.filename = None


    def pic_def(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open file', ' ', ' ')
        if self.filename[0] == '':
            print('No file is selected')
        else:
            open_file = self.filename[0]
            height = self.ui.pic_tag.height()
            width = self.ui.pic_tag.width()
            data = QPixmap(open_file)
            image = data.scaled(height, width)
            self.ui.pic_tag.setPixmap(image)

    def save_file_def(self):
        p = int(self.ui.pno_txt.text())
        n = self.ui.name_txt.text()
        pos = self.ui.posting_txt.text()
        try:
            pic_path = self.filename[0]
        except:
            pic_path = self.filename

        # print(p, n, pos)
        my_db_handle = sqlite3.connect("MY_DB.db")
        cur = my_db_handle.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS my_table (
                    id INTEGER PRIMARY KEY,
                    p_number INTEGER,
                    name TEXT,
                    place_of_posting TEXT,
                    notes TEXT,
                    pic_path TEXT
                    )
                """)
        cur.execute(""" INSERT INTO my_table (p_number, name, place_of_posting, notes, pic_path) VALUES(?,?,?,?,?)""", (p, n, pos, self.ui.notes_txt.text(), pic_path))
        my_db_handle.commit()
        my_db_handle.close()

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText('Information !')
        msg.setInformativeText('record saved')
        msg.setWindowTitle('Message Box')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()

        self.ui.pno_txt.clear()
        self.ui.name_txt.clear()
        self.ui.posting_txt.clear()
        self.ui.notes_txt.clear()
        self.ui.pic_tag.clear()

    def exit_func(self):
        self.close()


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = create_form_class()
    w.show()
    sys.exit(app.exec_())
