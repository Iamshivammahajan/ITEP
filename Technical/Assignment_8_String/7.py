def uppercase():
    sent = input("Enter a sentence: ")
    result = ""
    for ch in sent:
        if "a" <= ch <= "z":
            result += chr(ord(ch) - 32)
    else:
        result += ch
    print(result)
uppercase()

