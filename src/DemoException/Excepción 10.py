while True:
    try:
        lectura=input("Ingrese un numero entero: ")
        i_num = int(lectura)
        break
    except ValueError:
        print(f"Ingresaste: {lectura}, inténtelo de nuevo.")

print(f"Ingresaste el numero entero: {i_num}")