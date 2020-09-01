# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex1_graficos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import ex1_iconos_recursos


class Ui_Graficos(object):
    def setupUi(self, Graficos):
        Graficos.setObjectName("Graficos")
        Graficos.resize(640, 480)
        self.wdg_principal = QtWidgets.QWidget(Graficos)
        self.wdg_principal.setObjectName("wdg_principal")
        Graficos.setCentralWidget(self.wdg_principal)
        self.stt_principal = QtWidgets.QStatusBar(Graficos)
        self.stt_principal.setObjectName("stt_principal")
        Graficos.setStatusBar(self.stt_principal)
        self.tbr_principal = QtWidgets.QToolBar(Graficos)
        self.tbr_principal.setObjectName("tbr_principal")
        Graficos.addToolBar(QtCore.Qt.TopToolBarArea, self.tbr_principal)
        self.mniDibujarCirculo = QtWidgets.QAction(Graficos)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/circuloIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniDibujarCirculo.setIcon(icon)
        self.mniDibujarCirculo.setObjectName("mniDibujarCirculo")
        self.mniDibujarRectangulo = QtWidgets.QAction(Graficos)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Iconos/rectanguloIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniDibujarRectangulo.setIcon(icon1)
        self.mniDibujarRectangulo.setObjectName("mniDibujarRectangulo")
        self.mniDibujarLinea = QtWidgets.QAction(Graficos)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Iconos/lineaIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniDibujarLinea.setIcon(icon2)
        self.mniDibujarLinea.setObjectName("mniDibujarLinea")
        self.tbr_principal.addAction(self.mniDibujarCirculo)
        self.tbr_principal.addAction(self.mniDibujarRectangulo)
        self.tbr_principal.addAction(self.mniDibujarLinea)

        self.retranslateUi(Graficos)
        QtCore.QMetaObject.connectSlotsByName(Graficos)

    def retranslateUi(self, Graficos):
        _translate = QtCore.QCoreApplication.translate
        Graficos.setWindowTitle(_translate("Graficos", "Dibujar Figuras"))
        self.tbr_principal.setWindowTitle(_translate("Graficos", "toolBar"))
        self.mniDibujarCirculo.setText(_translate("Graficos", "Dibujar círculo"))
        self.mniDibujarCirculo.setToolTip(_translate("Graficos", "Dibujar círculo"))
        self.mniDibujarCirculo.setShortcut(_translate("Graficos", "Ctrl+C"))
        self.mniDibujarRectangulo.setText(_translate("Graficos", "Dibujar rectángulo"))
        self.mniDibujarRectangulo.setToolTip(_translate("Graficos", "Dibujar rectángulo"))
        self.mniDibujarRectangulo.setShortcut(_translate("Graficos", "Ctrl+R"))
        self.mniDibujarLinea.setText(_translate("Graficos", "Dibujar línea"))
        self.mniDibujarLinea.setToolTip(_translate("Graficos", "Dibujar línea"))
        self.mniDibujarLinea.setShortcut(_translate("Graficos", "Ctrl+L"))

