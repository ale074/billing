class medicina_animal:
    def __init__(self, animal, dosis )-> None:
        self.animal = animal
        self.dosis = dosis

    @property
    def animal(self):
        return self.animal

    @animal.setter
    def animal(self, animal):
        self.animal = animal 

    @property
    def dosis(self):
        return self.dosis

    @dosis.setter
    def frecuencia(self, dosis):
        self.dosis = dosis