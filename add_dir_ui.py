#Mini IDE
#Lang python
#By Imm0rtall
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_add_dir(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(303, 107)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 60, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 241, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Write name for directory"))
        self.pushButton.setText(_translate("Form", "Create"))