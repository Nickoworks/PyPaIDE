from PyQt5 import QtCore, QtGui, QtWidgets


class AboutDialog(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(215, 110)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 10, 91, 41))
        self.label.setStyleSheet("font-size:25px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 50, 71, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About PyPaIDE"))
        self.label.setText(_translate("Form", "PyPaIDE"))
        self.label_2.setText(_translate("Form", "By Immortall"))
        self.label_3.setText(_translate("Form", "Version 1.0"))
