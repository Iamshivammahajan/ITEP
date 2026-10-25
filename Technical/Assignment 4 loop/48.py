a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    i = 1
    print("Factors of", a, ":", end=" ")

    while i <= a:
        if a % i == 0:
            print(i, end=" ")
        i += 1

    print()
    a += 1