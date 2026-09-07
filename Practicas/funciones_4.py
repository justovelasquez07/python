grades = []

def addGrade(grade):
    grades.append(grade)

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

def showSize():
   return len(grades)

def showGrade():
   return (grades)

def getAverage():
   total = 0
   for grade in grades:
    total = total + grade
   return total / (showSize())

while True:
    try:
        grade = int(input("Ingrese su nota"))
        if grade >= 0 and grade <= 100:
         print("nota guardad:")
         addGrade(grade)
        else:
            print("valor invalio")
            continue
        answer = input("Quieres continuar:(S/N)")
        answer = answer.upper()
        if answer == "S":
          continue
        else:
            break
    except ValueError:
        print("su nota tiene que ser un numero entero")
        continue

print(f"Sus notas son:{showGrade()}")
print(f"El numero de notas son:{showSize()}")
print(f"Su promedio es:{getAverage()}")
print(f"La nota mas alta es:{maxGrade()}")
print(f"La nota mas baja es :{minGrade()}")