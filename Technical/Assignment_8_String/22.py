def secondfrequent():
    s="Shivam mahajan"
    freq={}
    max=float('-inf')
    max_2=float('-inf')

    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

    for ch in freq:
        if freq[ch]>max:
            max_2=max
            max=freq[ch]
        elif freq[ch]<max and freq[ch]>max_2:
            max_2=freq[ch]

    for ch in freq:
        if freq[ch]==max_2:
            print(ch,end=" ")
secondfrequent()