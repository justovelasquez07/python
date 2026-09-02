product_name = str(input("Enter the name of the product: "))
price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity: "))
subtotal = price * quantity

if subtotal >= 100: 
    print("Your discount is the 20%")
    discount = subtotal * 20 / 100
    total = subtotal - discount
    print("your total is: " + str(total))
elif subtotal >= 50:
    print("your dicount is the 10%")
    discount = subtotal * 10 / 100
    total = subtotal - discount
    print("your total is " + str(total))
else:
    total = subtotal 
    print("you do not have discount" + str(total) )

    

