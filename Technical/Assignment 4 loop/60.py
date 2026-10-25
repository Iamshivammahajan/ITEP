import math

n = int(input("Enter N: "))
i = 1

while i <= n:
    print("Number:", i)
    print("Square:", i ** 2)
    print("Cube:", i ** 3)
    print("Square Root:", math.sqrt(i))
    print()
    i += 1