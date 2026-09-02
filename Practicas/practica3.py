total = 0 
count = 0
for number in range(1,7):
    grade = float(input("Ingrese su nota: "))
    total = total + grade 
    if grade >= 60:
        print("pasate")
        count = count + 1
    else:
        print("No pasaste")

average = total / 6
print("Su promedio es de:" + str(average))
print("Estos pasaron: " + str(count))

