count = 0 

for number in range(1,11):
    name_product = str(input("Ingrese el nombre del producto: "))
    quantity = int(input("Ingresa la cantidad"))
    if quantity < 5:
        print("Tienes un stock muy bajo ")
        count = count + 1
    else:
        print("Producto guardado")

print("productos con menos stock" + str(count))