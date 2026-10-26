def charcteroccurance():
    sent = input("Enter a sentence: ")
    result = {}
    for ch in sent:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    print(result)
charcteroccurance() 