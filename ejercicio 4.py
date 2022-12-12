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
    def __init__(self, color, matricula, numero_ruedas, marca, en_marcha=False):
        self.color = color
        self.matricula = matricula
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.en_marcha = en_marcha

    def arrancar(self):
        self.en_marcha = True
        return

    def estado(self):
        if self.en_marcha:
            print("Está en marcha")
        else:
            print("Esta parada")
        return

    def __str__(self):
        return f"Marca: {self.marca}\nColor: {self.color}\nMatricula: {self.matricula}\nNumero de ruedas: {self.numero_ruedas}"


def main():
    motocicleta_kawasaki = motocicleta("verde", "13445-ASDF", 2, "Kawasaki")
    motocicleta_harley = motocicleta("negra", "12345-HJKL", 2, "Harley")
    print("-------------------------")
    print("Primera motocicleta:")
    print("-------------------------")
    print(motocicleta_kawasaki)
    motocicleta_kawasaki.estado()
    print("-------------------------")
    print("Segunda motocicleta:")
    print("-------------------------")
    print(motocicleta_harley)
    motocicleta_harley.arrancar()
    motocicleta_harley.estado()

    return


if __name__ == '__main__':
    main()
