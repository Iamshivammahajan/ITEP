n = int(input("Enter N: "))

i = 1
num = 0
sum = 0

while i <= n:
    num = num * 10 + 1
    sum = sum + num
    i = i + 1

print("Sum =", sum)