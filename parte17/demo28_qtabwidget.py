import sys

from PyQt5.QtWidgets import QApplication, QComboBox, QFormLayout, QHBoxLayout, QLineEdit, QPushButton, QRadioButton, QTabWidget, QWidget

class CapturaDatos(QTabWidget):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.setWindowTitle('Captura Datos Básicos')
        self.setFixedSize(300, 300)

        self.tab_datos_basicos = QWidget()
        self.tab_datos_contacto = QWidget()
        self.tab_datos_educacion = QWidget()

        self.addTab(self.tab_datos_basicos, 'Básicos')
        self.addTab(self.tab_datos_contacto, 'Contacto')
        self.addTab(self.tab_datos_educacion, 'Educación')

        self.inicializar_tab_datos_basicos()
        self.inicializar_tab_datos_contacto()
        self.inicializar_tab_datos_educacion()
    
    def inicializar_tab_datos_basicos(self):
        layout = QFormLayout()
        layout.addRow('Nombres:', QLineEdit())
        layout.addRow('Apellidos:', QLineEdit())

        lay_genero = QHBoxLayout()
        lay_genero.addWidget(QRadioButton('Hombre'))
        lay_genero.addWidget(QRadioButton('Mujer'))
        layout.addRow('Género:', lay_genero)

        self.tab_datos_basicos.setLayout(layout)


    def inicializar_tab_datos_contacto(self):
        layout = QFormLayout()
        layout.addRow('Correo-e:', QLineEdit())
        layout.addRow('Dirección:', QLineEdit())

        self.tab_datos_contacto.setLayout(layout)
    
    def inicializar_tab_datos_educacion(self):
        layout = QFormLayout()
        
        cbx_nivel_educativo = QComboBox()
        cbx_nivel_educativo.addItem('Primaria')
        cbx_nivel_educativo.addItem('Secundaria')
        cbx_nivel_educativo.addItem('Profesional')
        cbx_nivel_educativo.addItem('Maestría')
        cbx_nivel_educativo.addItem('Doctorado')

        layout.addRow('Nivel educativo:', cbx_nivel_educativo)
        layout.addRow('Profesión:', QLineEdit())
        layout.addRow('', QPushButton('Guardar datos'))

        self.tab_datos_educacion.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    ventana = CapturaDatos()
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
