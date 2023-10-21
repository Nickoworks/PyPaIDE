#Mini IDE
#Lang python
#By Imm0rtall
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_tools(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 139)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 10, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 40, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 40, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 10, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 70, 113, 32))
        self.pushButton_6.setText("Save File")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 40, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(230, 70, 113, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 70, 113, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 100, 113, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(120, 100, 221, 32))
        self.pushButton_11.setObjectName("pushButton_11")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tools"))
        self.pushButton.setText(_translate("Form", "Terminal"))
        self.pushButton_2.setText(_translate("Form", "Run And Save"))
        self.pushButton_3.setText(_translate("Form", "Delete File"))
        self.pushButton_4.setText(_translate("Form", "Add Dir"))
        self.pushButton_5.setText(_translate("Form", "Add File"))
        self.pushButton_7.setText(_translate("Form", "Edit File"))
        self.pushButton_8.setText(_translate("Form", "Set Editor"))
        self.pushButton_9.setText(_translate("Form", "Remove Dir"))
        self.pushButton_10.setText(_translate("Form", "Com Run"))
        self.pushButton_11.setText(_translate("Form", "Short Cuts"))
