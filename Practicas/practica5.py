total = 0

respuesta = input("Quieres seguir agreganso productos:(si/no)")

while respuesta == "si":
    name = str(input("Ingrese el nombre del producto:" ))
    precio = float(input("Ingrese el precio:"))
    cantidad = int(input("Ingrese la cantidad de producto"))
    subtotal = precio * cantidad
    total = total + subtotal
    respuesta = input("Quieres seguir agreganso productos:(si/no)")

print("Su total es de: " + str(total))