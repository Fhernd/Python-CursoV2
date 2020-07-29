# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo88_remocion_cuenta.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RemocionCuentaUsuario(object):
    def setupUi(self, RemocionCuentaUsuario):
        RemocionCuentaUsuario.setObjectName("RemocionCuentaUsuario")
        RemocionCuentaUsuario.resize(320, 240)
        RemocionCuentaUsuario.setMinimumSize(QtCore.QSize(320, 240))
        RemocionCuentaUsuario.setMaximumSize(QtCore.QSize(320, 240))
        self.verticalLayoutWidget = QtWidgets.QWidget(RemocionCuentaUsuario)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 5, 10, 30)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lbl_titulo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.lay_ver_principal.addWidget(self.lbl_titulo)
        self.lay_frm_datos = QtWidgets.QFormLayout()
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_correo_electronico = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_correo_electronico.setObjectName("lbl_correo_electronico")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_correo_electronico)
        self.txt_correo_electronico = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_correo_electronico.setObjectName("txt_correo_electronico")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_correo_electronico)
        self.lbl_clave = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_clave.setObjectName("lbl_clave")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_clave)
        self.txt_clave = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_clave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_clave.setObjectName("txt_clave")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_clave)
        self.btn_remover = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_remover.setObjectName("btn_remover")
        self.lay_frm_datos.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_remover)
        self.lay_ver_principal.addLayout(self.lay_frm_datos)

        self.retranslateUi(RemocionCuentaUsuario)
        QtCore.QMetaObject.connectSlotsByName(RemocionCuentaUsuario)

    def retranslateUi(self, RemocionCuentaUsuario):
        _translate = QtCore.QCoreApplication.translate
        RemocionCuentaUsuario.setWindowTitle(_translate("RemocionCuentaUsuario", "Remoción Cuenta de Usuario"))
        self.lbl_titulo.setText(_translate("RemocionCuentaUsuario", "Remover Cuenta de Usuario"))
        self.lbl_correo_electronico.setText(_translate("RemocionCuentaUsuario", "Correo electrónico:"))
        self.lbl_clave.setText(_translate("RemocionCuentaUsuario", "Contraseña:"))
        self.btn_remover.setText(_translate("RemocionCuentaUsuario", "Remover"))
