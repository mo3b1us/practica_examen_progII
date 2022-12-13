from tkinter import *

variables_names = ["Nombre", "Apellido", "Edad", "Correo", "Teléfono"]

variables = []
root = Tk()
datos = Frame(root)
datos.grid(row=0, column=0, padx=20, pady=0)

for index, variable in enumerate(variables_names):
    Label(datos, text=variable).grid(row=index, column=0, padx=10, pady=10)
    Entry(datos).grid(row=index, column=1, padx=10, pady=10)

boton = Frame(root)
boton.grid(row=1, column=0)
Label(boton, text="Mi botón").grid(row=0, column=0, padx=10, pady=10)
root.mainloop()