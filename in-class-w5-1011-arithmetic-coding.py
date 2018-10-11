def encode(s):
    arr = "".join(sorted(s))
    low = 0
    high = 1
    for c in s:
        range = high - low
        high = low + range * (arr.rindex(c)+1)/len(s)
        low = low + range * (arr.index(c)) / len(s)
    return low

print(encode("BILL GATES"))
