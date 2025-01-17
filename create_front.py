# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_front.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 442)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 30, 154, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(90, 340, 75, 23))
        self.save_btn.setObjectName("save_btn")
        self.exit_btn = QtWidgets.QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(230, 340, 75, 23))
        self.exit_btn.setObjectName("exit_btn")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 80, 217, 74))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pno_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.pno_txt.setObjectName("pno_txt")
        self.gridLayout.addWidget(self.pno_txt, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.name_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.name_txt.setObjectName("name_txt")
        self.gridLayout.addWidget(self.name_txt, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.posting_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.posting_txt.setObjectName("posting_txt")
        self.gridLayout.addWidget(self.posting_txt, 2, 1, 1, 1)
        self.pic_tag = QtWidgets.QLabel(Dialog)
        self.pic_tag.setGeometry(QtCore.QRect(400, 70, 91, 71))
        self.pic_tag.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pic_tag.setAutoFillBackground(True)
        self.pic_tag.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_tag.setObjectName("pic_tag")
        self.pic_btn = QtWidgets.QPushButton(Dialog)
        self.pic_btn.setGeometry(QtCore.QRect(410, 150, 75, 23))
        self.pic_btn.setObjectName("pic_btn")
        self.open_record = QtWidgets.QPushButton(Dialog)
        self.open_record.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.open_record.setObjectName("open_record")
        self.del_record = QtWidgets.QPushButton(Dialog)
        self.del_record.setGeometry(QtCore.QRect(330, 300, 75, 23))
        self.del_record.setObjectName("del_record")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 190, 76, 20))
        self.label_5.setObjectName("label_5")
        self.notes_txt = QtWidgets.QLineEdit(Dialog)
        self.notes_txt.setGeometry(QtCore.QRect(160, 160, 133, 91))
        self.notes_txt.setObjectName("notes_txt")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 280, 156, 41))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_label = QtWidgets.QLabel(self.widget)
        self.comboBox_label.setObjectName("comboBox_label")
        self.gridLayout_2.addWidget(self.comboBox_label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Employee Record"))
        self.save_btn.setText(_translate("Dialog", "save"))
        self.exit_btn.setText(_translate("Dialog", "exit"))
        self.label.setText(_translate("Dialog", "P No"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Place of posting"))
        self.pic_tag.setText(_translate("Dialog", "Picture"))
        self.pic_btn.setText(_translate("Dialog", "Picture"))
        self.open_record.setText(_translate("Dialog", "Open"))
        self.del_record.setText(_translate("Dialog", "Delete"))
        self.label_5.setText(_translate("Dialog", "Notes"))
        self.comboBox_label.setText(_translate("Dialog", "Existing Records"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
