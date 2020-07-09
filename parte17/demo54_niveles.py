# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo54_niveles.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Niveles(object):
    def setupUi(self, Niveles):
        Niveles.setObjectName("Niveles")
        Niveles.resize(435, 360)
        Niveles.setMinimumSize(QtCore.QSize(435, 360))
        Niveles.setMaximumSize(QtCore.QSize(435, 360))
        self.verticalLayoutWidget = QtWidgets.QWidget(Niveles)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1, 1, 431, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay_ver_principal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_ver_principal.setContentsMargins(10, 10, 10, 0)
        self.lay_ver_principal.setObjectName("lay_ver_principal")
        self.lay_frm_azucar_presion_arterial = QtWidgets.QFormLayout()
        self.lay_frm_azucar_presion_arterial.setHorizontalSpacing(60)
        self.lay_frm_azucar_presion_arterial.setVerticalSpacing(20)
        self.lay_frm_azucar_presion_arterial.setObjectName("lay_frm_azucar_presion_arterial")
        self.lbl_nivel_azucar = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nivel_azucar.setObjectName("lbl_nivel_azucar")
        self.lay_frm_azucar_presion_arterial.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_nivel_azucar)
        self.hsb_nivel_azucar = QtWidgets.QScrollBar(self.verticalLayoutWidget)
        self.hsb_nivel_azucar.setOrientation(QtCore.Qt.Horizontal)
        self.hsb_nivel_azucar.setObjectName("hsb_nivel_azucar")
        self.lay_frm_azucar_presion_arterial.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hsb_nivel_azucar)
        self.lbl_presion_arterial = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_presion_arterial.setObjectName("lbl_presion_arterial")
        self.lay_frm_azucar_presion_arterial.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_presion_arterial)
        self.hsd_presion_arterial = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.hsd_presion_arterial.setOrientation(QtCore.Qt.Horizontal)
        self.hsd_presion_arterial.setObjectName("hsd_presion_arterial")
        self.lay_frm_azucar_presion_arterial.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hsd_presion_arterial)
        self.lay_ver_principal.addLayout(self.lay_frm_azucar_presion_arterial)
        self.lay_hor_pulso_nivel_colesterol = QtWidgets.QHBoxLayout()
        self.lay_hor_pulso_nivel_colesterol.setObjectName("lay_hor_pulso_nivel_colesterol")
        self.lbl_pulso = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_pulso.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_pulso.setObjectName("lbl_pulso")
        self.lay_hor_pulso_nivel_colesterol.addWidget(self.lbl_pulso)
        self.vsb_pulso = QtWidgets.QScrollBar(self.verticalLayoutWidget)
        self.vsb_pulso.setOrientation(QtCore.Qt.Vertical)
        self.vsb_pulso.setObjectName("vsb_pulso")
        self.lay_hor_pulso_nivel_colesterol.addWidget(self.vsb_pulso)
        self.lbl_nivel_colesterol = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_nivel_colesterol.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_nivel_colesterol.setObjectName("lbl_nivel_colesterol")
        self.lay_hor_pulso_nivel_colesterol.addWidget(self.lbl_nivel_colesterol)
        self.vsd_nivel_colesterol = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.vsd_nivel_colesterol.setOrientation(QtCore.Qt.Vertical)
        self.vsd_nivel_colesterol.setObjectName("vsd_nivel_colesterol")
        self.lay_hor_pulso_nivel_colesterol.addWidget(self.vsd_nivel_colesterol)
        self.lay_ver_principal.addLayout(self.lay_hor_pulso_nivel_colesterol)
        self.txt_resultado = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_resultado.setReadOnly(True)
        self.txt_resultado.setObjectName("txt_resultado")
        self.lay_ver_principal.addWidget(self.txt_resultado)

        self.retranslateUi(Niveles)
        QtCore.QMetaObject.connectSlotsByName(Niveles)

    def retranslateUi(self, Niveles):
        _translate = QtCore.QCoreApplication.translate
        Niveles.setWindowTitle(_translate("Niveles", "Niveles"))
        self.lbl_nivel_azucar.setText(_translate("Niveles", "Nivel de azúcar:"))
        self.lbl_presion_arterial.setText(_translate("Niveles", "Presión arterial:"))
        self.lbl_pulso.setText(_translate("Niveles", "Pulso:"))
        self.lbl_nivel_colesterol.setText(_translate("Niveles", "Nivel de colesterol:"))
