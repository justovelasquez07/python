name = input("Enter your name: ")
grade = float(input("Enter your grade: "))

if grade >= 0 and grade <= 59:
    print("Failed")

elif grade >= 60 and grade <= 69:
    print("Passed")

elif grade >= 70 and grade <= 79:
    print("Good")

elif grade >= 80 and grade <= 89:
    print("Very good")

elif grade >= 90 and grade <= 100:
    print("Excellent")

else:
    print("Invalid grade")