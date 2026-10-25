n = int(input("Enter number: "))
original = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** 3
    n //= 10

if sum == original:
    print("Armstrong number")
else:
    print("Not Armstrong number")