num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Enter choice (+, >, ==): ")

if choice == "+":
    print("Addition:", num1 + num2)

elif choice == ">":
    if num1 > num2:
        print(num1, "is greater")
    else:
        print(num2, "is greater")

elif choice == "==":
    if num1 == num2:
        print("Both numbers are equal")
    else:
        print("Numbers are not equal")

else:
    print("Invalid choice")