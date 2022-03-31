class Factura:
    def __init__(self, id_factura, list_products) -> None:
        self.id_factura = id_factura
        self.list_products = list_products


    @property
    def id_factura(self):
        return self.id_factura

    @id_factura.setter
    def id_factura(self, id_factura):
        self.id_factura = id_factura

    @property
    def list_products(self):
        return self.list_products

    @list_products.setter
    def list_products(self, list_products):
        self.list_products = list_products