"""Ejercicio 4: Definir una clase motocicleta, con las siguientes propiedades: marca, color,
matricula, numero de ruedas y en_marcha.
1. Definir comportamientos para los futuros objetos que pertenezcan a esta clase, que
vienen determinados por distintos métodos (arrancar…):
2. Construir 2 objetos de la clase motocicleta y acceder a las propiedades de dicha clase.
3. Dentro de las funciones de los métodos arrancar, habrá otro método llamado “Estado”
, el cual dependerá si el método “arrancar” es = TRUE, el método de estado dirá que la
motocicleta esta en Marcha, en caso contrario, quiere decir que está Parada (stop).
4. Imprimir los dos objetos, uno en marcha y otro parado con sus respectivos atributos
de cada Objeto (Marca, color, ruedas y en marcha o no.)"""


class motocicleta:
    motor = False

    def __init__(self, color, matricula, numero_ruedas, marca):
        self.marca = marca
        self.color = color
        self.matricula = matricula
        self.numero_ruedas = numero_ruedas

    def arrancar(self):
        if self.motor:
            print("Esta en marcha")
        else: print("Esta parada")
    
    def estado(self):
        print("Marca:", self.marca, "\nColor:", self.color, "\nMatricula:", self.matricula, "\nNumero de ruedas:", self.numero_ruedas,"\n")

def main():
    motocicleta_kawasaki = motocicleta("verde", "13445-ASDF", 2, "Kawasaki")
    motocicleta_kawasaki.motor = True
    motocicleta_harley = motocicleta("negra", "12345-HJKL", 2, "Harley")
    print("Primera motocicleta:")
    motocicleta_kawasaki.arrancar()
    motocicleta_kawasaki.estado()
    print("Segunda motocicleta:")
    motocicleta_harley.arrancar()
    motocicleta_harley.estado()

if __name__ == '__main__':
    main()