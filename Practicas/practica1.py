total = 0 
mayor = 0 

for number in range (1,6):
    venta = int(input("Ingresa la cantidad vendidad:"))
    total = total + venta
    if venta > mayor:
        mayor = venta
print("total de ventas:" + str(total))
print("venta mayor fue:" + str(mayor))
