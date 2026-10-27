def mostfrequent():
    str = input("Enter a string: ")
    result = {}
    for ch in str:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    max_freq = 0
    for ch in result:
        if result[ch] > max_freq:
            max_freq = result[ch]
            max_char = ch
    print(f"The most frequent character is {max_char} and its frequency is {max_freq}")
mostfrequent()