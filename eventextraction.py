# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventextraction.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.eventextraction = QtWidgets.QLabel(self.centralwidget)
        self.eventextraction.setGeometry(QtCore.QRect(70, 40, 311, 51))
        self.eventextraction.setObjectName("eventextraction")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 140, 511, 151))
        self.lineEdit.setObjectName("lineEdit")
        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(40, 100, 211, 31))
        self.input.setObjectName("input")
        self.pushme = QtWidgets.QPushButton(self.centralwidget)
        self.pushme.setGeometry(QtCore.QRect(210, 340, 151, 41))
        self.pushme.setObjectName("pushme")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 410, 521, 171))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(40, 380, 131, 21))
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Event Extraction"))
        self.eventextraction.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Event Extraction</span></p></body></html>"))
        self.input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#55aa00;\">Input Text</span></p></body></html>"))
        self.pushme.setText(_translate("MainWindow", "RUN"))
        self.output.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Output</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

