
grades = []

def addGrade(grade):
    grades.append(grade)

def maxGrade():
    maxGrade = grades[0]
    for grade in grades:
        if grade > maxGrade:
            maxGrade = grade
    return maxGrade

def minGrade ():
    minGrade = grades[0]
    for grade in grades:
        if grade < minGrade:
            minGrade = grade
    return minGrade

def showSize():
    return len(grades)

def showGrade():
    return grade

while True:
    try:
        grade = int(input("Ingrese la nota: "))
        addGrade(grade)
    except ValueError:
        print("Ingrese numeros enteros")
        continue

    answer = input("Quiere continuar:(S/N)")
    answer = answer.upper()

    if answer == "S":
        continue
    else:
        break

print(f"su notas son:{showGrade()}")
print(f"su numeros de notas es:{showSize()}")
print(f"la nota mayor es :{maxGrade()}")
print(f"la nota menor es:{minGrade()}")



    




        


