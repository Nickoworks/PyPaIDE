#Mini IDE
#Lang python
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_save(object):
    def setupUi(self, Form_save):
        Form_save.setObjectName("Form_save")
        Form_save.resize(240, 88)
        self.pushButton = QtWidgets.QPushButton(Form_save)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form_save)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 211, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Form_save)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 201, 26))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form_save)
        QtCore.QMetaObject.connectSlotsByName(Form_save)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Write file name for save..."))
        self.pushButton.setText(_translate("Form", "Save"))
