from Numeros_naturales import Numeros_naturales

if __name__ == '__main__':
    num = Numeros_naturales(0)
    num.leer_numero()
    print("Número:", num.numero)
    print("Divisores:", num.calcular_divisores())

    print("\n===========================")
    num.numero = 12
    print("Número:", num.numero)
    print("Divisores:", num.calcular_divisores())
