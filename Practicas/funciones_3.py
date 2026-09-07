grades =[]

def addgrade(grade):
    grades.append(grade)

def getAverage():
    total = 0 
    for grade in grades:
        total = total + grade
    return total /(showSize())   

def showSize():
    return len(grades)

def showGrade():
    return grades

def maxGrade():
    maxGrade = grades[0]
    for grade in grades:
        if grade > maxGrade:
            maxGrade = grade
    return maxGrade

def minGrade():
    minGrade = grades[0]
    for grade in grades:
        if grade < minGrade:
            minGrade = grade
    return minGrade

while True:
    try:
        grade = int(input("Ingrese su nota: "))
        addgrade(grade)
    except ValueError:
        print("Tiene que ser numero entero")
        continue
    answer = input("Quieres continuar:(S/N)")
    answer = answer.upper()

    if answer == "S":
        continue
    else:
        break

print(f"Sus notas son:{showGrade()}")
print(f"El numero de notas son:{showSize()}")
print(f"Su promedio es:{getAverage()}")
print(f"La nota mas alta es:{maxGrade()}")
print(f"La nota mas baja es :{minGrade()}")





