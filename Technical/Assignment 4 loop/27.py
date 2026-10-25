n = int(input("Enter N: "))

i = 1

while i <= n:
    if i % 2 == 1:
        print("*", end=" ")
    else:
        print("#", end=" ")
    i = i + 1