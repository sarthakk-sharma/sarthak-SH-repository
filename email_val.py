# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'em_val.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 183)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 110, 161, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.in_email = QtWidgets.QLineEdit(Dialog)
        self.in_email.setGeometry(QtCore.QRect(50, 70, 171, 21))
        self.in_email.setObjectName("in_email")
        self.emalval = QtWidgets.QLabel(Dialog)
        self.emalval.setGeometry(QtCore.QRect(50, 20, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Himalaya")
        font.setPointSize(18)
        self.emalval.setFont(font)
        self.emalval.setObjectName("emalval")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.emalval.setText(_translate("Dialog", "Enter E- Mail to be validated"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())