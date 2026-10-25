a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    original = a
    n = a
    sum = 0

    while n > 0:
        digit = n % 10
        sum += digit ** 3
        n //= 10

    if sum == original:
        print(a)

    a += 1