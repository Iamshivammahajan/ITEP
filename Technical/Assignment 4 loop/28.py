n = int(input("Enter N: "))

i = 1

while i <= n:
    if i % 5 == 0:
        print("Hello", end=" ")
    else:
        print(i, end=" ")
    i = i + 1