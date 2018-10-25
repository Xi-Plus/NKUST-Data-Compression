def encode(s, table=None):
    arr = "".join(sorted(s))
    if table is None:
        table = {}
        for c in s:
            table[c] = [(arr.index(c)) / len(s), (arr.rindex(c)+1)/len(s)]
    low = 0
    high = 1
    send = []
    for c in s:
        range = high - low
        high = low + range * table[c][1]
        low = low + range * table[c][0]
        tsend = ""
        while True:
            if low < 0.5 and high < 0.5:
                tsend += "0"
                low *= 2
                high *= 2
            elif low >= 0.5 and high >= 0.5:
                tsend += "1"
                low = abs(low - 0.5) * 2
                high = abs(high - 0.5) * 2
            else:
                break
        send.append(tsend)
    send.append("1")
    return {"table": table, "send": send}

res = encode("BILL GATES")
print(res["table"])
print(res["send"])
print()

res = encode("1321", {"1": [0, 0.8], "2": [0.8, 0.82], "3": [0.82, 1]})
print(res["table"])
print(res["send"])
