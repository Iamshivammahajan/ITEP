n = int(input("Enter number: "))
original = n
sum = 0

while n > 0:
    digit = n % 10

    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1

    sum += fact
    n //= 10

if sum == original:
    print("Strong number")
else:
    print("Not a strong number")