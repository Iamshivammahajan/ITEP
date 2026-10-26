def check_palindrome():
    n = input("Enter a string: ")
    rev = ""
    for ch in n:
        rev = ch + rev
    if rev == n:
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")
check_palindrome()

    