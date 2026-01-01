import numpy as np

class Simulador:
    @classmethod
    def dados(cls, caras_dado, cantidad_dados=1):
        cls.caras_dado = caras_dado
        cls.cantidad_dados=cantidad_dados
    
    @classmethod
    def lanzamientos(cls, cantidad_lanzamientos=1000000):
        return np.random.randint(1,cls.caras_dado+1,size=(cantidad_lanzamientos,cls.cantidad_dados))
