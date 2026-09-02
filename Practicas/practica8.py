try:
    precio = float(input("Ingrese el precio:"))
except ValueError:
    print("Datos incorrecto")
else:
    print("Precio registrado ")