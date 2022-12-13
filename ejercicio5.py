import tkinter
import openpyxl


def introducir_info(datos):
    for campo, dato in datos.items():
        valor = dato.get()
        print(f"{campo} = {valor}")
    return


def main():
    window = tkinter.Tk()
    window.title("Introducción de la información del usuario")

    frame = tkinter.Frame(window)
    frame.pack()

    user_info_frame = tkinter.LabelFrame(frame, text="Información del usuario")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    variable_names = ["Nombre", "Apellido", "Edad", "Correo", "Teléfono"]
    datos = dict()
    for index, variable in enumerate(variable_names):
        etiqueta = tkinter.Label(user_info_frame, text=variable)
        etiqueta.grid(row=index, column=0, padx=10, pady=10)

        espacio_escritura = tkinter.Entry(user_info_frame)
        espacio_escritura.grid(row=index, column=1, padx=10, pady=10)

        datos[variable] = espacio_escritura

    button = tkinter.Button(frame, text="Introducir información", command=lambda: introducir_info(datos))
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    window.mainloop()
    return


if __name__ == '__main__':
    main()
