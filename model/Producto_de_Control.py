from model.Producto import Producto

class Producto_de_Control(Producto):
    def __init__(self, iCA, frecuencia) -> None:
        self.iCA = iCA
        self.frecuencia = frecuencia

    @property
    def iCA(self):
        return self.iCA

    @iCA.setter
    def iCA(self, iCA):
        self.iCA = iCA 

    @property
    def frecuencia(self):
        return self.frecuencia

    @frecuencia.setter
    def frecuencia(self, frecuencia):
        self.frecuencia = frecuencia