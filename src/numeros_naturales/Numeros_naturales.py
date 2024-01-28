class Numeros_naturales:
    def __init__(self, numero):
        self.numero = numero

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def calcular_divisores(self):
        divisores = []
        for i in range(1, self.numero + 1):
            if self.numero % i == 0:
                divisores.append(i)
        return divisores

if __name__ == '__main__':
    num = Numeros_naturales(12)
    print("Número:", num.get_numero())
    print("Divisores:", num.calcular_divisores())