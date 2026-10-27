def longestword():
    str = input("Enter a string: ")
    s = str.split()
    max = 0
    for word in s:
        if len(word) > max:
            max = len(word)
            max_word = word
    print(f"The longest word is {max_word} and its length is {max}")
longestword()