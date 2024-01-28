class Numeros_naturales:
    def __init__(self, numero):
        self._numero = numero

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._numero = valor-3
        else:
            raise ValueError("El número debe ser un entero no negativo.")

    def leer_numero(self):
        while True:
            try:
                nuevo_numero = int(input("Ingrese un número natural: "))
                if nuevo_numero < 0:
                    print("Por favor, ingrese un número natural válido.")
                else:
                    self._numero = nuevo_numero
                    break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def calcular_divisores(self):
        divisores = []
        for i in range(1, self._numero + 1):
            if self._numero % i == 0:
                divisores.append(i)
        return divisores


if __name__ == '__main__':
    num = Numeros_naturales(12)
    print("Número:", num.get_numero())
    print("Divisores:", num.calcular_divisores())
