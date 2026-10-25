n = int(input("Enter N: "))

i = 1

while i <= n:
    if i % 2 == 1:
        print(chr(64 + i), end=" ")
    else:
        print(chr(96 + i), end=" ")
    i = i + 1