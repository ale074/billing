class Producto:
    def __init__(self, id, nombre, precio) -> None:
        self.id = id
        self.nombre = nombre
        self.precio = precio

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = id

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def precio(self):
        return self.precio

    @precio.setter
    def precio(self, precio):
        self.precio = precio
