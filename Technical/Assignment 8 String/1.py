n = input("Enter a string: ")
rev = ""
for ch in n:
    rev = ch + rev
print(f"The reverse of {n} is {rev}")
