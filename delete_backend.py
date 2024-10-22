import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog
from create_front import *  # <-- Add file name
import sqlite3
class delete_form_class(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog() # <-- Add window name here
        self.ui.setupUi(self)
        #‘’’Add your code here’’’
        self.setWindowTitle('DELETE RECORD')
        self.ui.del_record.setDisabled(True)
        self.ui.save_btn.setDisabled(True)
        self.filename = None

        #connections
        self.ui.open_record.clicked.connect(self.load_record)
        self.ui.del_record.clicked.connect(self.del_record)
        #self.ui.save_btn.clicked.connect(self.save_file_def)
        self.ui.exit_btn.clicked.connect(self.exit_func)
        self.ui.pic_btn.clicked.connect(self.pic_def)
        self.ui.name_txt.setReadOnly(True)
        self.ui.pno_txt.setReadOnly(True)
        self.ui.posting_txt.setReadOnly(True)
        self.ui.notes_txt.setReadOnly(True)
        self.ui.del_record.setDisabled(True)
        self.fresh_form()

    def del_record(self):
        #for sqlite
        my_db_handle = sqlite3.connect("MY_DB.db")
        cur = my_db_handle.cursor()
        print(int(self.ui.pno_txt.text()))
        cur.execute('DELETE FROM my_table WHERE p_number = ?', (int(self.ui.pno_txt.text()),))
        print('here')
        my_db_handle.commit()
        my_db_handle.close()

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText('Information !')
        msg.setInformativeText('record deleted')
        msg.setWindowTitle('Message Box')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        self.fresh_form()

    def empty_form_msg(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText('Information !')
        msg.setInformativeText('No record found in data base. Please create a record first')
        msg.setWindowTitle('Message Box')
        # msg.setWindowIcon(QIcon(r‘icon location'))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()

    def fresh_form(self):
        #with sqlite
        my_db_handle = sqlite3.connect("MY_DB.db")
        cur = my_db_handle.cursor()
        cur.execute('SELECT p_number FROM my_table')
        rows = cur.fetchall()
        my_db_handle.close()
        self.ui.comboBox.clear()
        if len(rows) < 1:
            self.ui.open_record.setDisabled(True)
            self.empty_form_msg()
            self.close()

        for idx in rows:
            self.ui.comboBox.addItem(str(idx).lstrip('(').rstrip(')').rstrip(','))

        self.ui.pno_txt.clear()
        self.ui.name_txt.clear()
        self.ui.posting_txt.clear()
        self.ui.pic_tag.clear()
        self.ui.notes_txt.clear()
        self.ui.del_record.setDisabled(True)
        self.ui.save_btn.setDisabled(True)

    def load_record(self):
        #following lines are for sqlite
        selected_value = self.ui.comboBox.currentText()
        my_db_handle = sqlite3.connect("MY_DB.db")
        cur = my_db_handle.cursor()
        cur.execute("SELECT DISTINCT p_number, name, place_of_posting, notes, pic_path FROM my_table WHERE p_number = ?", (int(selected_value),))
        data = (cur.fetchall()[0])
        my_db_handle.close()
        self.ui.pno_txt.setText(str(data[0]))
        self.ui.name_txt.setText(str(data[1]))
        self.ui.posting_txt.setText(str(data[2]))
        self.ui.notes_txt.setText(str(data[3]))
        self.filename = str(data[4])
        self.pic_def()
        self.ui.del_record.setEnabled(True)

    def pic_def(self):
        #self.filename = QFileDialog.getOpenFileName(self, 'Open file', ' ', ' ')
        if self.filename == '':
            print('No file is selected')
        else:
            open_file = self.filename
            #print(self.filename[0])
            height = self.ui.pic_tag.height()
            width = self.ui.pic_tag.width()
            data = QPixmap(open_file)
            image = data.scaled(height, width)
            self.ui.pic_tag.setPixmap(image)

    def exit_func(self):
        self.close()


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = delete_form_class()
    w.show()
    sys.exit(app.exec_())
