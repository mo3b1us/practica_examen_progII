import tkinter
import openpyxl


def introducir_info(datos):
    for campo, dato in datos.items():
        valor = dato.get()
        print(f"{campo} = {valor}")
    return


def guardar_fich():
    return


def main():
    window = tkinter.Tk()
    window.title("Introducción de la información del usuario")
    window.resizable(False, False)
    window.iconbitmap('AppIcon.ico')
    frame = tkinter.Frame(window)
    frame.grid(row=0, column=0)

    # LabelFrame con la opcion de introducir datos dentro de frame
    user_info_frame = tkinter.LabelFrame(frame, text="Información del usuario")
    user_info_frame.config(bg="burlywood1")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    variable_names = ["Nombre", "Apellido", "Edad", "Correo", "Teléfono"]
    datos = dict()
    for index, variable in enumerate(variable_names):
        etiqueta = tkinter.Label(user_info_frame, text=variable, bg="burlywood1")
        etiqueta.grid(row=index, column=0, padx=10, pady=10)

        espacio_escritura = tkinter.Entry(user_info_frame)
        espacio_escritura.grid(row=index, column=1, padx=10, pady=10)

        datos[variable] = espacio_escritura

    # Boton de guardado dentro de frame
    button_agregar = tkinter.Button(frame, text="Introducir información", command=lambda: introducir_info(datos), bg="gainsboro")
    button_agregar.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    # LabelFrame con la opcion de guardar dentro de frame
    save_info_frame = tkinter.LabelFrame(frame)
    save_info_frame.config(bg="lightblue")
    save_info_frame.grid(row=0, column=1, padx=20, pady=10)

    etiqueta = tkinter.Label(save_info_frame, text="Ingrese nombre del archivo", bg="lightblue", )
    etiqueta.grid(row=0, column=0, padx=10, pady=10)

    espacio_escritura = tkinter.Entry(save_info_frame)
    espacio_escritura.grid(row=1, column=0, padx=10, pady=10)

    button_agregar = tkinter.Button(save_info_frame, text="Guardar", command=guardar_fich, bg="gainsboro")
    button_agregar.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    # Boton de salir dentro de frame
    button_salir = tkinter.Button(frame, text="Salir", command=window.destroy, bg="gainsboro")
    button_salir.grid(row=1, column=1, sticky="news", padx=20, pady=10)

    window.mainloop()
    return


if __name__ == '__main__':
    main()
