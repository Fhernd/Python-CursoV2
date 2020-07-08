# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo49_inicio_sesion.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InicioSesion(object):
    def setupUi(self, InicioSesion):
        InicioSesion.setObjectName("InicioSesion")
        InicioSesion.resize(320, 198)
        self.wdg_principal = QtWidgets.QWidget(InicioSesion)
        self.wdg_principal.setObjectName("wdg_principal")
        self.lbl_datos_acceso = QtWidgets.QLabel(self.wdg_principal)
        self.lbl_datos_acceso.setGeometry(QtCore.QRect(105, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_datos_acceso.setFont(font)
        self.lbl_datos_acceso.setObjectName("lbl_datos_acceso")
        self.formLayoutWidget = QtWidgets.QWidget(self.wdg_principal)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 57, 301, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.frm_lay_inicio_sesion = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.frm_lay_inicio_sesion.setContentsMargins(0, 0, 0, 0)
        self.frm_lay_inicio_sesion.setObjectName("frm_lay_inicio_sesion")
        self.lbl_nombre_usuario = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_nombre_usuario.setObjectName("lbl_nombre_usuario")
        self.frm_lay_inicio_sesion.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_usuario)
        self.txt_nombre_usuario = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_nombre_usuario.setObjectName("txt_nombre_usuario")
        self.frm_lay_inicio_sesion.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_usuario)
        self.lbl_contrasegnia = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_contrasegnia.setObjectName("lbl_contrasegnia")
        self.frm_lay_inicio_sesion.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_contrasegnia)
        self.txt_contrasegnia = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_contrasegnia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_contrasegnia.setObjectName("txt_contrasegnia")
        self.frm_lay_inicio_sesion.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_contrasegnia)
        self.btn_iniciar_sesion = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_iniciar_sesion.setObjectName("btn_iniciar_sesion")
        self.frm_lay_inicio_sesion.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_iniciar_sesion)
        InicioSesion.setCentralWidget(self.wdg_principal)
        self.menubar = QtWidgets.QMenuBar(InicioSesion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        InicioSesion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InicioSesion)
        self.statusbar.setObjectName("statusbar")
        InicioSesion.setStatusBar(self.statusbar)

        self.retranslateUi(InicioSesion)
        QtCore.QMetaObject.connectSlotsByName(InicioSesion)

    def retranslateUi(self, InicioSesion):
        _translate = QtCore.QCoreApplication.translate
        InicioSesion.setWindowTitle(_translate("InicioSesion", "Inicio Sesión"))
        self.lbl_datos_acceso.setText(_translate("InicioSesion", "Datos de Acceso"))
        self.lbl_nombre_usuario.setText(_translate("InicioSesion", "Nombre de usuario:"))
        self.lbl_contrasegnia.setText(_translate("InicioSesion", "Contraseña:"))
        self.btn_iniciar_sesion.setText(_translate("InicioSesion", "Iniciar Sesión"))
