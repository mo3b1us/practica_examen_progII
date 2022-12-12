""" Crear un programa que tenga el siguiente menú:
1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la
posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
3. Longitud de la lista: te muestra el número de elementos de la lista.
4. Eliminar el último número: Muestra el último número de la lista y lo borra.
5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella
(la posición se pide a partir de 1).
6. Contar números: Te pide un número y te dice cuántas apariciones hay en la lista.
7. Posiciones de un número: Te pide un número y te dice en que posiciones está
(contando desde 1).
8. Mostrar números: Muestra los números de la lista
9. Salir """


def insertar_inicio(numeros):
    numeros.insert(0, int(input("Introduzca el número a añadir: ")))
    return


def insertar_posicion(numeros):
    numeros.insert(int(input("Introduzca la posición el la que añadir el número (empezando por el 1): ")) - 1,
                   int(input("Introduzca el número a añadir: ")))
    return


def longitud(numeros):
    print(f"La longitud de la lista es: {len(numeros)}")
    return


def eliminar_ultimo(numeros):
    numeros.pop(len(numeros) - 1)
    return


def eliminar_posicion(numeros):
    try:
        numeros.pop(int(input("Introduzca la posición a eliminar (empezando por el 1):")) - 1)
    except IndexError:
        print("Índice fuera del rango")
    return


def contar(numeros):
    numeros.count(int(input("Introduzca el número a contar: ")))
    return


def posiciones(numeros):
    numero_buscar = int(input("Número a buscar y sacar posiciones: "))
    if numero_buscar in numeros:
        print(f"Lista con las posiciones en las que aparece el {numero_buscar}: ")
        print([idx + 1 for idx, numero in enumerate(numeros) if numero == numero_buscar])
    else:
        print("El numero a buscar no estaba en la lista.")
    return


def mostrar(numeros):
    print(numeros)
    return


def main():
    numeros = []
    opc = "default"
    while opc != "9":
        print("""Menu principal
    
1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la
posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
3. Longitud de la lista: te muestra el número de elementos de la lista.
4. Eliminar el último número: Muestra el último número de la lista y lo borra.
5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella
(la posición se pide a partir de 1).
6. Contar números: Te pide un número y te dice cuántas apariciones hay en la lista.
7. Posiciones de un número: Te pide un número y te dice en que posiciones está
(contando desde 1).
8. Mostrar números: Muestra los números de la lista
9. Salir """)
        opc = input("Introduzca opción: ")  # clave de mi diccionario de opciones
        # Declaración de un diccionario cuyas claves son las opciones posibles
        # y cuyos valores son las funciones a llamar
        opciones = {
            "1": lambda: insertar_inicio(numeros),
            "2": lambda: insertar_posicion(numeros),
            "3": lambda: longitud(numeros),
            "4": lambda: eliminar_ultimo(numeros),
            "5": lambda: eliminar_posicion(numeros),
            "6": lambda: contar(numeros),
            "7": lambda: posiciones(numeros),           
            "8": lambda: mostrar(numeros),
            "9": lambda: print("Gracias por usar nuestro programa. Finalizando programa . . ."),
            "default": lambda: print("Opción no reconocida. Por favor vuelva a elegir opción.")
        }
        opciones.get(opc, opciones["default"])()  # llamada a la función que obtenemos a partir de la clave opc
        print()  # Simplemente, añado una línea para que quede separado
    return


if __name__ == '__main__':
    main()
