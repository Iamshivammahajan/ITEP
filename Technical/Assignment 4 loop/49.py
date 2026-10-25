a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    i = 1
    sum = 0

    while i < a:
        if a % i == 0:
            sum += i
        i += 1

    if sum == a:
        print(a)

    a += 1