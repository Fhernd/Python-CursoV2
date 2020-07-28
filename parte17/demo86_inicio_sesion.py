# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo86_inicio_sesion.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InicioSesion(object):
    def setupUi(self, InicioSesion):
        InicioSesion.setObjectName("InicioSesion")
        InicioSesion.resize(320, 200)
        InicioSesion.setMinimumSize(QtCore.QSize(320, 200))
        InicioSesion.setMaximumSize(QtCore.QSize(320, 200))
        self.verticalLayoutWidget = QtWidgets.QWidget(InicioSesion)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 20, 10, 40)
        self.lay_ver_principal.setSpacing(10)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lbl_titulo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.lay_ver_principal.addWidget(self.lbl_titulo)
        self.lay_frm_inicio_sesion = QtWidgets.QFormLayout()
        self.lay_frm_inicio_sesion.setObjectName("lay_frm_inicio_sesion")
        self.lbl_correo_electronico = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_correo_electronico.setObjectName("lbl_correo_electronico")
        self.lay_frm_inicio_sesion.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_correo_electronico)
        self.txt_correo_electronico = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_correo_electronico.setObjectName("txt_correo_electronico")
        self.lay_frm_inicio_sesion.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_correo_electronico)
        self.lbl_clave = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_clave.setObjectName("lbl_clave")
        self.lay_frm_inicio_sesion.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_clave)
        self.txt_clave = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_clave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_clave.setObjectName("txt_clave")
        self.lay_frm_inicio_sesion.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_clave)
        self.btn_iniciar_sesion = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_iniciar_sesion.setObjectName("btn_iniciar_sesion")
        self.lay_frm_inicio_sesion.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_iniciar_sesion)
        self.lay_ver_principal.addLayout(self.lay_frm_inicio_sesion)

        self.retranslateUi(InicioSesion)
        QtCore.QMetaObject.connectSlotsByName(InicioSesion)

    def retranslateUi(self, InicioSesion):
        _translate = QtCore.QCoreApplication.translate
        InicioSesion.setWindowTitle(_translate("InicioSesion", "Inicio Sesión"))
        self.lbl_titulo.setText(_translate("InicioSesion", "Inicio de Sesión"))
        self.lbl_correo_electronico.setText(_translate("InicioSesion", "Correo electrónico:"))
        self.lbl_clave.setText(_translate("InicioSesion", "Contraseña:"))
        self.btn_iniciar_sesion.setText(_translate("InicioSesion", "Iniciar sesión"))
