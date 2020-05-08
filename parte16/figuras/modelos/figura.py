from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color_fondo, color_borde):
        self.color_fondo = color_fondo
        self.color_borde = color_borde
    
    @abstractmethod
    def dibujar(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'Color fondo: {self.color_fondo} - Color borde: {self.color_borde}'
