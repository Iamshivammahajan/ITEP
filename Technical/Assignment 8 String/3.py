def checkvowelandconsonant():
    n = input("Enter a string: ")
    vowels = 0
    consonant = 0
    for ch in n:
        if ch in "aeiouAEIOU":
            vowels += 1
        elif ch in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonant += 1
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonant}")
checkvowelandconsonant()