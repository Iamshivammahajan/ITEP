def length():
    sent = input("Enter a sentence: ")
    count = 0
    for ch in sent:
        count += 1
    print(f"Length of {sent} is : {count}")
length()
