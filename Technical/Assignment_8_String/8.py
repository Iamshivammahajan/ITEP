def removespace():
    sent = input("Enter a string: ")
    result = ""
    for ch in sent:
        if ch != " ":
            result += ch
    print(result)
removespace()