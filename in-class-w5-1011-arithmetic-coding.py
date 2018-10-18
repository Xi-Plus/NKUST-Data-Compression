def encode(s):
    arr = "".join(sorted(s))
    table = {}
    for c in s:
    	table[c] = [(arr.index(c)) / len(s), (arr.rindex(c)+1)/len(s)]
    low = 0
    high = 1
    for c in s:
        range = high - low
        high = low + range * (arr.rindex(c)+1)/len(s)
        low = low + range * (arr.index(c)) / len(s)
    return {"table": table, "value": low}

def decode(table, value):
	res = ""
	while value > 1e-7:
		for c in table:
			if value >= table[c][0] and value < table[c][1]:
				res += c
				value -= table[c][0]
				value /= (table[c][1] - table[c][0])
				break
	return res

res = encode("BILL GATES")
print(res["table"])
print(res["value"])

print(decode(res["table"], res["value"]))
