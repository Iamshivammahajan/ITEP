a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    fact = 1
    i = 1

    while i <= a:
        fact *= i
        i += 1

    print("Factorial of", a, "=", fact)
    a += 1