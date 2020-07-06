# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parte17\demo38_saludo_qt_designer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 248)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_saludar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saludar.setGeometry(QtCore.QRect(180, 90, 75, 23))
        self.btn_saludar.setObjectName("btn_saludar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.mbr_principal = QtWidgets.QMenuBar(MainWindow)
        self.mbr_principal.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.mbr_principal.setObjectName("mbr_principal")
        MainWindow.setMenuBar(self.mbr_principal)
        self.sbr_estado = QtWidgets.QStatusBar(MainWindow)
        self.sbr_estado.setObjectName("sbr_estado")
        MainWindow.setStatusBar(self.sbr_estado)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Saludo"))
        self.btn_saludar.setToolTip(_translate("MainWindow", "Saluda al usuario"))
        self.btn_saludar.setText(_translate("MainWindow", "Saludar"))
