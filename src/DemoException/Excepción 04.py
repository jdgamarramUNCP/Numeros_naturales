a = 10
b = -1
try:
    if a < 0 or b < 0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Por favor, ingrese un valor válido")
