count = 0
total = 0
while True:
    name_product = str(input("Ingrese el nombre del producto: (salir)"))
    if name_product == "salir":
        break
    price = float(input("Ingrese el precio: "))
    quantity = int(input("Ingrese la cantidad: "))
    if quantity <= 0:
        print("Cantidad invalida")
        continue

    subtotal = price * quantity
    total = total + subtotal
    count = count + 1
    if subtotal >= 1000:
        print("venta grande")

    


print("Su cantidad es: " + str(total))
print("La cantidad de ventas es: " + str(count))

