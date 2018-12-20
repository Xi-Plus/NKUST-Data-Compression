m = 8

data = [
[139,144,149,153,155,155,155,155],
[144,151,153,156,159,156,156,156],
[150,155,160,163,158,156,156,156],
[159,161,162,160,160,159,159,159],
[159,160,161,162,162,155,155,155],
[161,161,161,161,160,157,157,157],
[162,162,161,163,162,157,157,157],
[162,162,161,161,163,158,158,158],
]
minp = min(sum(data, []))
maxp = max(sum(data, []))

delta = (maxp - minp) / m
print(minp, maxp, delta)

for r in range(len(data)):
	for c in range(len(data[r])):
		level = int((data[r][c]-minp) / delta)
		if level == m:
			level -= 1
		print(int((level+0.5)*delta+minp+0.5), end=" ")
	print()
