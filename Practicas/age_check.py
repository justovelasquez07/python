name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if age >= 0 and age <= 17:
    print("You are a minor.")
elif age >= 18:
    print("Do you have permission? yes or not ")
    permission = input()
    if permission == "yes":
        print("you can accede")
    else:
         print("you can not accede")





 
