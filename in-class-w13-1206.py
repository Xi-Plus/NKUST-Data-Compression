import numpy as np
import math


x = np.array([
	[65,170],
	[75,188],
	[60,150],
	[70,170],
	[56,130],
	[80,203],
	[68,160],
	[50,110],
	[40,80],
	[50,153],
	[69,148],
	[62,140],
	[76,164],
	[64,120],
])

m = 2.5

phi = math.atan(m)
print("phi", math.degrees(phi))

A = np.array([
	[math.cos(phi), math.sin(phi)],
	[-math.sin(phi), math.cos(phi)],
])

print(A)

y = np.dot(A, x.T).T
print(y)

y = np.array([[a[0], 0] for a in y])

print(y)

A2 = np.linalg.inv(A)
print(A2)

y = np.dot(A2, y.T).T
print(y)

# print(np.transpose(a))

# print(np.dot(c, d))

# print(np.dot(a, b))
