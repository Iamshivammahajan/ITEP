a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    i = 1

    while i <= 10:
        print(a, "x", i, "=", a * i)
        i += 1

    print()
    a += 1