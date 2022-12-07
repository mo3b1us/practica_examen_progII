""" Ejercicio 1:
Desarrollar un programa que permita crear una lista de palabras y que, a continuación, me presente un menú con las siguientes opciones: 
1. Contar: Me pide una palabra (cadena), y me dice cuántas veces aparece en la lista 
2. Modificar: Me pide una palabra(cadena), y otra cadena a modificar, y modifica todas a las apariciones de la primera por la
segunda en la lista. 
3. Eliminar: Me pide una cadena, y la elimina de la lista. 
4. Mostrar: Muestra la lista de cadenas 
5. Terminar """

def contar():
    buscar_palabra = str(input("Introduzca palabra a buscar: "))
    contador = 0
    for i in lista:
        if i == buscar_palabra:
            contador += 1
    print(f"La palabra '{buscar_palabra}' aparece {contador} veces")

def modificar():
    buscar_palabra = str(input("Introduzca la palabra a sustituir: "))
    sustituir_palabra = str(input("Introduzca la palabra por la que sustituir: "))
    for i in range(len(lista)):
        if lista[i] == buscar_palabra:
            lista[i] = sustituir_palabra

def eliminar():
    buscar_palabra = str(input("Introduzca la palabra a eliminar: "))
    lista.remove(buscar_palabra)

def mostrar():
    print(f"La lista es {lista}")



    

cantidad_palabras = int(input("¿Cuántas palabras tiene la lista?: "))
if cantidad_palabras < 1:
    print("Cantidad de palabras errónea")
else:
    lista = []
    for i in range(cantidad_palabras):
        palabra = input(f"Introduzca la {i+1} palabra:" )
        lista += [palabra]
opc = "default"


while opc != "5":  # Programa principal
    print("""Menu principal

1- Contar: Me pide una palabra (cadena), y me dice cuántas veces aparece en la lista 
2- Modificar: Me pide una palabra(cadena), y otra cadena a modificar, y modifica todas a 
las apariciones de la primera por la segunda en la lista. 
3- Eliminar: Me pide una cadena, y la elimina de la lista. 
4- Mostrar: Muestra la lista de cadenas 
5- Salir """)
    opc = input("Introduzca opción: ")  # clave de mi diccionario de opciones
    # Declaración de un diccionario cuyas claves son las opciones posibles
    # y cuyos valores son las funciones a llamar
    opciones = {
        "1": contar,
        "2": modificar,
        "3": eliminar,
        "4": mostrar,
        "5": lambda: print("Gracias por usar nuestro programa. Finalizando programa . . ."),
        "default": lambda: print("Opción no reconocida. Por favor vuelva a elegir opción.")
    }
    opciones.get(opc, opciones["default"])()  # llamada a la función que obtenemos a partir de la clave opc
    print()  # Simplemente, añado una línea para que quede separado