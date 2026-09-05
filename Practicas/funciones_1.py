precios = []

def addprice(precio):
    precios.append(precio)

def getMaxPrice():
    maxPrice = precios[0]
    for precio in precios:
        if precio > maxPrice:
            maxPrice = precio
    return maxPrice

def getMinPrice():
    minPrice = precios[0]
    for precio in precios:
        if precio < minPrice:
            minPrice = precio
    return minPrice

def showSize ():
    return len(precios)
    
def showPrice():
    return precios

while True:
    try:
        precio = float(input("Ingrese el precio: "))
        addprice(precio)
    except ValueError:   
       print("El precio debe ser un número")

    answer =  input("Quiere continuar: (S/N)" )
    answer = answer.upper()
    if answer == "S":
            continue
    else:
            break
print(f"La cantidad de precios son: {showSize()}")
print(f"Los precios son:  {showPrice()}")
print(f"El precio mas alto es: {getMaxPrice()}")
print(f"El precio mas bajo es: {getMinPrice()}")











