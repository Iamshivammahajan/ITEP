def find1standlast():
    sent = input("Enter a sentence: ")
    if sent:
        print(f"1st character: {sent[0]}")
        print(f"Last character: {sent[-1]}")
    else:
        print(f"Empty String")
find1standlast()