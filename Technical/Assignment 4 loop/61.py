a = int(input("Enter first year: "))
b = int(input("Enter second year: "))

while a <= b:
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
        print(a)

    a += 1