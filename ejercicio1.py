""" Ejercicio 1:
Desarrollar un programa que permita crear una lista de palabras y que, a continuación, me presente un menú con las siguientes opciones: 
1. Contar: Me pide una palabra (cadena), y me dice cuántas veces aparece en la lista 
2. Modificar: Me pide una palabra(cadena), y otra cadena a modificar, y modifica todas a las apariciones de la primera por la
segunda en la lista. 
3. Eliminar: Me pide una cadena, y la elimina de la lista. 
4. Mostrar: Muestra la lista de cadenas 
5. Terminar """


def contar(lista):
    n = lista.count(buscada := input("Introduzca palabra a buscar: "))
    print(f"La palabra '{buscada}' aparece {n} veces.")
    return


def modificar(lista):
    sustituto = input("Introduzca la palabra sustituto: ")
    if (buscada := input("Introduzca la palabra en la lista que quiere sustituir: ")) in lista:
        for index, palabra in enumerate(lista):
            if palabra == buscada:
                lista[index] = sustituto
        print(f"Todas las coincidencias con la palabra '{buscada}' fueron sustituidas por la palabra '{sustituto}'.")
    else:
        print(f"La palabra '{buscada}' no estaba en la lista.")
    return


def eliminar(lista):
    if (eliminada := input("Introduzca la palabra a eliminar: ")) in lista:
        lista.remove(eliminada)
        print(f"La palabra '{eliminada}' fue eliminada de la lista.")
    else:
        print(f"La palabra '{eliminada}' no estaba en la lista.")
    return


def mostrar(lista):
    print(f"La lista es: {lista}")
    return


# Programa principal
def main():
    while (num := int(input("¿Cuántas palabras tiene la lista?: "))) < 1:
        print("Cantidad de palabras errónea. Por favor repita la operación.")
    palabras = [input(f"Introduzca la {i + 1}º palabra: ") for i in range(num)]

    opc = "default"
    while opc != "5":
        print("""Menu principal
    
    1- Contar: Me pide una palabra (cadena), y me dice cuántas veces aparece en la lista 
    2- Modificar: Me pide una palabra(cadena), y otra cadena a modificar, y modifica todas a 
    las apariciones de la primera por la segunda en la lista. 
    3- Eliminar: Me pide una cadena, y la elimina de la lista. 
    4- Mostrar: Muestra la lista de cadenas 
    5- Terminar """)
        opc = input("Introduzca opción: ")  # clave de mi diccionario de opciones
        # Declaración de un diccionario cuyas claves son las opciones posibles
        # y cuyos valores son las funciones a llamar
        opciones = {
            "1": lambda: contar(palabras),
            "2": lambda: modificar(palabras),
            "3": lambda: eliminar(palabras),
            "4": lambda: mostrar(palabras),
            "5": lambda: print("Gracias por usar nuestro programa. Finalizando programa . . ."),
            "default": lambda: print("Opción no reconocida. Por favor vuelva a elegir opción.")
        }
        opciones.get(opc, opciones["default"])()  # llamada a la función que obtenemos a partir de la clave opc
        print()  # Simplemente, añado una línea para que quede separado
    return


if __name__ == '__main__':
    main()
