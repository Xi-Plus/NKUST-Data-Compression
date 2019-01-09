import numpy as np


data = np.array([
[80, -3, -1, 0, 0, 0, 0, 0],
[-2, -2, -1, 0, 0, 0, 0, 0],
[-1, -1, 0, 0, 0, 0, 0, 0],
[-1, -2, 0, 0, 0, 0, 0, 0],
[-1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
])

res = []
for i in range(1-data.shape[0], data.shape[0]):
	res.append(np.diagonal(data[::-1,:], i)[::int((-1)**(i+1))])
res = np.concatenate(res)

print(res)
