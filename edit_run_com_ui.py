#Mini IDE
#Lang python
#By Imm0rtall
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_edit_run_com(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(173, 91)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Run Com Cfg"))
        self.pushButton.setText(_translate("Form", "Save"))
