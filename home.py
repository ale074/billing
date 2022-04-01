from tkinter import *

from numpy import product
from services.facturas_services import Facturas_services
from services.Products_services import Products_services
from share.Table import Table

class Home:
    def __init__(self, win) -> None:
        self.listar_facturas = Button(win, text="Listar Facturas", fg="blue", command=self.listar)
        self.agregar_productos = Button(win, text="Agregar Productos", fg="blue", command=self.agregar)
        self.listar_facturas.place(x=90, y=100)
        self.agregar_productos.place(x=80, y=150)
        self.win = win

    def listar(self):
        facturas = Facturas_services.get_facturas()
        print("llega")
        print(facturas)

    def agregar(self):
        self.destroy_element(self.listar_facturas)
        self.destroy_element(self.agregar_productos)
        productos = {
                    "fertilizantes": Products_services.get_all_products_fertilizantes(),
                    "control_de_plagas": Products_services.get_all_products_control_de_plagas(),
                    "medicina_animal": Products_services.get_all_products_medicina_animal(),
        }
        t = Table(self.win, len(productos), len(productos[0]), productos['fertilizantes'])


    def destroy_element(self, element):
        element.destroy()
        



window=Tk()
mywin=Home(window)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop() 
