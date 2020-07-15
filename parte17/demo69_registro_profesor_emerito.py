# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo69_registro_profesor_emerito.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_RegistroProfesorEmerito(object):
    def setupUi(self, RegistroProfesorEmerito):
        RegistroProfesorEmerito.setObjectName("RegistroProfesorEmerito")
        RegistroProfesorEmerito.resize(320, 185)
        RegistroProfesorEmerito.setMinimumSize(QtCore.QSize(320, 185))
        RegistroProfesorEmerito.setMaximumSize(QtCore.QSize(320, 185))
        self.formLayoutWidget = QtWidgets.QWidget(RegistroProfesorEmerito)
        self.formLayoutWidget.setGeometry(QtCore.QRect(5, 6, 311, 164))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.lay_frm_datos = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.lay_frm_datos.setContentsMargins(10, 10, 10, 0)
        self.lay_frm_datos.setObjectName("lay_frm_datos")
        self.lbl_identidad = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_identidad.setObjectName("lbl_identidad")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_identidad)
        self.txt_identidad = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_identidad.setObjectName("txt_identidad")
        self.lay_frm_datos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_identidad)
        self.lbl_nombre_completo = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_nombre_completo.setObjectName("lbl_nombre_completo")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre_completo)
        self.txt_nombre_completo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_nombre_completo.setObjectName("txt_nombre_completo")
        self.lay_frm_datos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_nombre_completo)
        self.lbl_telefono = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_telefono.setObjectName("lbl_telefono")
        self.lay_frm_datos.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_telefono)
        self.txt_telefono = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_telefono.setObjectName("txt_telefono")
        self.lay_frm_datos.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_telefono)
        self.lbl_especialidad = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_especialidad.setObjectName("lbl_especialidad")
        self.lay_frm_datos.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_especialidad)
        self.cbx_especialidades = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbx_especialidades.setObjectName("cbx_especialidades")
        self.cbx_especialidades.addItem("")
        self.cbx_especialidades.addItem("")
        self.cbx_especialidades.addItem("")
        self.cbx_especialidades.addItem("")
        self.cbx_especialidades.addItem("")
        self.cbx_especialidades.addItem("")
        self.cbx_especialidades.addItem("")
        self.lay_frm_datos.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbx_especialidades)
        self.lbl_reconocimiento = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_reconocimiento.setObjectName("lbl_reconocimiento")
        self.lay_frm_datos.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_reconocimiento)
        self.txt_reconocimiento = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_reconocimiento.setObjectName("txt_reconocimiento")
        self.lay_frm_datos.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_reconocimiento)
        self.btn_registrar = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_registrar.setObjectName("btn_registrar")
        self.lay_frm_datos.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.btn_registrar)

        self.retranslateUi(RegistroProfesorEmerito)
        QtCore.QMetaObject.connectSlotsByName(RegistroProfesorEmerito)

    def retranslateUi(self, RegistroProfesorEmerito):
        _translate = QtCore.QCoreApplication.translate
        RegistroProfesorEmerito.setWindowTitle(_translate("RegistroProfesorEmerito", "Profesor Emérito - Registro"))
        self.lbl_identidad.setText(_translate("RegistroProfesorEmerito", "Identidad:"))
        self.lbl_nombre_completo.setText(_translate("RegistroProfesorEmerito", "Nombre completo:"))
        self.lbl_telefono.setText(_translate("RegistroProfesorEmerito", "Teléfono:"))
        self.lbl_especialidad.setText(_translate("RegistroProfesorEmerito", "Especialidad:"))
        self.cbx_especialidades.setItemText(0, _translate("RegistroProfesorEmerito", "Computación"))
        self.cbx_especialidades.setItemText(1, _translate("RegistroProfesorEmerito", "Biología"))
        self.cbx_especialidades.setItemText(2, _translate("RegistroProfesorEmerito", "Medicina"))
        self.cbx_especialidades.setItemText(3, _translate("RegistroProfesorEmerito", "Astronomía"))
        self.cbx_especialidades.setItemText(4, _translate("RegistroProfesorEmerito", "Geología"))
        self.cbx_especialidades.setItemText(5, _translate("RegistroProfesorEmerito", "Literatura"))
        self.cbx_especialidades.setItemText(6, _translate("RegistroProfesorEmerito", "Música"))
        self.lbl_reconocimiento.setText(_translate("RegistroProfesorEmerito", "Reconocimiento:"))
        self.btn_registrar.setText(_translate("RegistroProfesorEmerito", "Registrar"))
