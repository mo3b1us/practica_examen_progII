"""Ejercicio 2
En un equipo de corredores se quiere guardar el nombre de los corredores que entrenan, y los kilómetros que entrenan
cada día de la semana.
Se habrá de utilizar dos arreglos:
Nombre_Corredor: Lista para guardar los nombres de los corredores.
Kilómetros: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que entrena cada
corredor.
Al finalizar se muestra la lista con los nombres de Corredores y los kilómetros que ha realizado.
"""
import random


class Corredor:
    def __init__(self, nombre, kms):
        self.nombre = nombre
        self.kms_dia = dict(zip(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], kms))

    # Definimos la propiedad total_kms que nos devuelve la suma de kms del corredor a lo largo de la semana
    @property
    def total_kms(self):
        return sum(self.kms_dia.values())

    # El método __str__ nos permite representar al objeto cuando se pasa a la función print()
    def __str__(self):
        return f"{self.nombre} ha realizado {self.total_kms} km en total."


def tabla(corredores):
    print("---------------------------------------------------------------------", end="")
    print("\n|\tNombre\t|", end="")
    semana = ["L", "M", "X", "J", "V", "S", "D"]
    for dia in semana:
        print(f"\t{dia}\t|", end="")
    print("\n---------------------------------------------------------------------")

    for corredor in corredores:
        print(f"|\t{corredor.nombre}\t|", end="")
        for kms in corredor.kms_dia.values():
            print(f"\t{kms}\t|", end="")
        print()
    print("---------------------------------------------------------------------")
    return


def main():
    Nombre_Corredor = ["Javier", "Pedro", "Luis", "Pepe", "Alfonso"]
    # Generamos una lista con listas de 7 elementos que contienen los km que ha realizado cada dia cada corredor
    kilometros = [[random.randint(0, 4) * 5 for dia in range(7)] for corredor in Nombre_Corredor]

    # Generamos una lista de objetos instanciados de la clase Corredor
    corredores = [Corredor(nombre, kms) for nombre, kms in zip(Nombre_Corredor, kilometros)]

    # Obtenemos el total de kms de cada corredor con la propiedad total_kms
    total_kms = [corredor.total_kms for corredor in corredores]

    tabla(corredores)

    print("Corredores:")
    for corredor in corredores:
        print(corredor)


if __name__ == '__main__':
    main()

