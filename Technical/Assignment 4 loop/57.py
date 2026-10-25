a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    i = 2
    count = 0

    while i < a:
        if a % i == 0:
            count += 1
        i += 1

    if a > 1 and count == 0:
        print(a)

    a += 1