class ControlDePlagas:
    def __init__(self, periodo_de_carencia)-> None:
        self.periodo_de_carencia = periodo_de_carencia


    @property
    def periodo_de_carencia(self):
        return self.periodo_de_carencia

    @periodo_de_carencia.setter
    def periodo_de_carencia(self, fecha_de_aplicacion):
        self.periodo_de_carencia = fecha_de_aplicacion 