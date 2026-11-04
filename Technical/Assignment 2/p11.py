age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ")
marital = input("Enter marital status (Y/N): ")

if sex == "F":
    print("Work in urban areas only")
elif sex == "M" and age >= 20 and age < 40:
    print("Can work anywhere")
elif sex == "M" and age >= 40 and age <= 60:
    print("Work in urban areas only")
else:
    print("ERROR")