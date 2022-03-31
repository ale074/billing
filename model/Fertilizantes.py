class Fertilizantes:
    def __init__(self, fecha_de_aplicacion)-> None:
        self.fecha_de_aplicacion = fecha_de_aplicacion


    @property
    def fecha_de_aplicacion(self):
        return self.fecha_de_aplicacion

    @fecha_de_aplicacion.setter
    def fecha_de_aplicacion(self, fecha_de_aplicacion):
        self.fecha_de_aplicacion = fecha_de_aplicacion 
