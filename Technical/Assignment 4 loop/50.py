a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    original = a
    n = a
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    if original == rev:
        print(a)

    a += 1