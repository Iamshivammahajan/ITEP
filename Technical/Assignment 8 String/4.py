def count():
    n = input("Enter a string: ")
    uppercase = 0
    lowercase = 0
    digits = 0
    specialcharacters = 0
    for ch in n:
        if "A" <= ch <= "Z":
            uppercase += 1
        elif "a" <= ch <= "z":
            lowercase += 1
        elif "0" <= ch <= "9":
            digits += 1
    else:
        specialcharacters += 1
    print(f"Uppercase: {uppercase}")
    print(f"Lowercase: {lowercase}")
    print(f"Digits: {digits}")
    print(f"Special Characters: {specialcharacters}")
count()     