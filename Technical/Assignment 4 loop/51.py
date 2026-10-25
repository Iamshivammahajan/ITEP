a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a <= b:
    n = a
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    print(a, "->", rev)
    a += 1