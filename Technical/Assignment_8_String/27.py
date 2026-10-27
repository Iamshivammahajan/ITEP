#Find all duplicate characters and their frequencies.
def dupli_freq():
    str = input("Enter a string: ")
    result = {}
    for ch in str:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    for ch in result:
        if result[ch] > 1:
            print(f"Character: {ch}, Frequency: {result[ch]}")
dupli_freq()