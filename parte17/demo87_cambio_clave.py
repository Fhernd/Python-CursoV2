# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo87_cambio_clave.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CambioClave(object):
    def setupUi(self, CambioClave):
        CambioClave.setObjectName("CambioClave")
        CambioClave.resize(320, 240)
        CambioClave.setMinimumSize(QtCore.QSize(320, 240))
        CambioClave.setMaximumSize(QtCore.QSize(320, 240))
        self.verticalLayoutWidget = QtWidgets.QWidget(CambioClave)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setSpacing(10)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lbl_cambio_clave = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_cambio_clave.setFont(font)
        self.lbl_cambio_clave.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_cambio_clave.setObjectName("lbl_cambio_clave")
        self.lay_ver_principal.addWidget(self.lbl_cambio_clave)
        self.lay_frm_cambio_clave = QtWidgets.QFormLayout()
        self.lay_frm_cambio_clave.setObjectName("lay_frm_cambio_clave")
        self.lbl_correo_electronico = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_correo_electronico.setObjectName("lbl_correo_electronico")
        self.lay_frm_cambio_clave.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_correo_electronico)
        self.txt_correo_electronico = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_correo_electronico.setObjectName("txt_correo_electronico")
        self.lay_frm_cambio_clave.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_correo_electronico)
        self.lbl_clave_actual = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_clave_actual.setObjectName("lbl_clave_actual")
        self.lay_frm_cambio_clave.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_clave_actual)
        self.txt_clave_actual = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_clave_actual.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_clave_actual.setObjectName("txt_clave_actual")
        self.lay_frm_cambio_clave.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_clave_actual)
        self.lbl_nueva_clave = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nueva_clave.setObjectName("lbl_nueva_clave")
        self.lay_frm_cambio_clave.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_nueva_clave)
        self.txt_nueva_clave = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nueva_clave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_nueva_clave.setObjectName("txt_nueva_clave")
        self.lay_frm_cambio_clave.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_nueva_clave)
        self.lbl_nueva_clave_repetir = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nueva_clave_repetir.setObjectName("lbl_nueva_clave_repetir")
        self.lay_frm_cambio_clave.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_nueva_clave_repetir)
        self.txt_nueva_clave_repetir = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_nueva_clave_repetir.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_nueva_clave_repetir.setObjectName("txt_nueva_clave_repetir")
        self.lay_frm_cambio_clave.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_nueva_clave_repetir)
        self.btn_cambiar_clave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cambiar_clave.setObjectName("btn_cambiar_clave")
        self.lay_frm_cambio_clave.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.btn_cambiar_clave)
        self.lay_ver_principal.addLayout(self.lay_frm_cambio_clave)

        self.retranslateUi(CambioClave)
        QtCore.QMetaObject.connectSlotsByName(CambioClave)

    def retranslateUi(self, CambioClave):
        _translate = QtCore.QCoreApplication.translate
        CambioClave.setWindowTitle(_translate("CambioClave", "Cambio de Contraseña"))
        self.lbl_cambio_clave.setText(_translate("CambioClave", "Cambio de Contraseña"))
        self.lbl_correo_electronico.setText(_translate("CambioClave", "Correo electrónico:"))
        self.lbl_clave_actual.setText(_translate("CambioClave", "Contraseña actual:"))
        self.lbl_nueva_clave.setText(_translate("CambioClave", "Nueva contraseña:"))
        self.lbl_nueva_clave_repetir.setText(_translate("CambioClave", "Nueva contraseña (repetir):"))
        self.btn_cambiar_clave.setText(_translate("CambioClave", "Cambiar contraseña"))
