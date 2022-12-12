import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl


window = tkinter.Tk()
window.title("Introducción de la información del usuario")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame =tkinter.LabelFrame(frame, text="Información del usuario")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

nombre_etiqueta = tkinter.Label(user_info_frame, text="Nombre")
nombre_etiqueta.grid(row=0, column=0)
apellido_etiqueta = tkinter.Label(user_info_frame, text="Apellido")
apellido_etiqueta.grid(row=0, column=1)
edad_etiqueta = tkinter.Label(user_info_frame, text="Edad")
edad_etiqueta.grid(row=2, column=0)
telefono_etiqueta = tkinter.Label(user_info_frame, text="Telefono")
telefono_etiqueta.grid(row=2, column=1)
correo_etiqueta = tkinter.Label(user_info_frame, text="Correo")
correo_etiqueta.grid(row=4, column=0)

entrada_nombre = tkinter.Entry(user_info_frame)
entrada_apellido = tkinter.Entry(user_info_frame)
entrada_edad = tkinter.Entry(user_info_frame)
entrada_correo = tkinter.Entry(user_info_frame)
entrada_telefono = tkinter.Entry(user_info_frame)
entrada_nombre.grid(row=1, column=0)
entrada_apellido.grid(row=1, column=1)
entrada_edad.grid(row=3, column=0)
entrada_telefono.grid(row=3, column=1)
entrada_correo.grid(row=5, column=0)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
def introducirInformacion():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()

    if nombre and apellido:
        edad = entrada_edad.get()
        telefono = entrada_telefono.get()
        correo = entrada_correo.get()

        print("Nombre ", nombre, "Apellido: ", apellido)
        print("Edad: ", edad)
        print("Teléfono: ", telefono, "Correo: ", correo)
        print("------------------------------------------")

        filepath = "Users\Rubén\Desktop"

        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ["Nombre", "Apellido", "Edad", "Correo", "Teléfono"]
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([nombre, apellido, edad, correo, telefono])
        workbook.save(filepath)


# Boton
button = tkinter.Button(frame, text="Introducir información", command= introducirInformacion)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()