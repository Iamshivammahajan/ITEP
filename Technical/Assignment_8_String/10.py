def replace():
    sent = input("Enter a sentence: ")
    result = ""
    for ch in sent:
        if ch == " ":
            result += "-"
        else:
            result += ch
    print(result)
replace()
