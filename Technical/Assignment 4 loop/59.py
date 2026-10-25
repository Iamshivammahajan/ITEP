n = 100
sum = 0

while n <= 200:
    if n % 9 == 0:
        sum += n
    n += 1

print("Sum:", sum)