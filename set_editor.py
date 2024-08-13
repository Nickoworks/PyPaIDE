#Mini IDE
#Lang python
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_set_editor(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(264, 120)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(150, 30, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 10, 60, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 60, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Set Editor"))
        self.radioButton.setText(_translate("Form", "Italic text"))
        self.label.setText(_translate("Form", "Font size"))
        self.pushButton.setText(_translate("Form", "Save"))
