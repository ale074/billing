from tkinter import *

class Home:
    def __init__(self, win) -> None:
        self.listar_facturas = Button(win, text="Listar Facturas", fg="blue", command=self.listar)
        self.agregar_productos = Button(win, text="Agregar Productos", fg="blue")
        self.listar_facturas.place(x=90, y=100)
        self.agregar_productos.place(x=80, y=150)

    def listar(self):
        self.destroy_element(self.listar_facturas)
        self.destroy_element(self.agregar_productos)

    def getFacturas(self):
        pass


    def destroy_element(self, element):
        element.destroy()
        



window=Tk()
mywin=Home(window)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop() 
