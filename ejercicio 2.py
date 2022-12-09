"""Ejercicio 2
En un equipo de corredores se quiere guardar el nombre de los corredores que entrenan, y los kilómetros que entrenan 
cada día de la semana. 
Se habrá de utilizar dos arreglos: 
Nombre_Corredor: Lista para guardar los nombres de los corredores. 
kilometros: Tabla para guardar los kilómetros que realizan cada día de la semana. 
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que entrena cada 
corredor. 
Al finalizar se muestra la lista con los nombres de Corredores y los kilómetros que ha realizado. 
"""

def main():
    while ((num := int(input("¿Cuantos corredores tiene la lista?: "))) < 1 & (dias := int(input("¿Cuántos días a la semana corren? "))) < 1):
        print("Cantidad de corredores o de días errónea. Por favor repita la operación.")
    nombre_corredor = [input(f"Introduzca el {i + 1}º corredor: ") for i in range(num)]
    kilometros_corredor = [int(input(f"Introduzca los km del {i + 1}º corredor el {j+1} día: ")) for j in range(dias) for i in range(num)]
    kilometros = [[nombre_corredor],[kilometros_corredor]]
    aux, j = 0, 0
    total_kms = []
    while(j < num):
        for i in range(j,len(kilometros_corredor),num):
            aux += kilometros_corredor[i]
        total_kms.append(aux)
        print(f"{nombre_corredor[j]} - {total_kms[j]} kms")
        aux = 0
        j += 1

if __name__ == '__main__':
    main()