import numpy

m1=[
[0.5,   0,   0,   0, 0.5,   0,   0,   0],
[0.5,   0,   0,   0,-0.5,   0,   0,   0],
[  0, 0.5,   0,   0,   0, 0.5,   0,   0],
[  0, 0.5,   0,   0,   0,-0.5,   0,   0],
[  0,   0, 0.5,   0,   0,   0, 0.5,   0],
[  0,   0, 0.5,   0,   0,   0,-0.5,   0],
[  0,   0,   0, 0.5,   0,   0,   0, 0.5],
[  0,   0,   0, 0.5,   0,   0,   0,-0.5],
]
m2=[
[0.5,   0, 0.5,   0,   0,   0,   0,   0],
[0.5,   0,-0.5,   0,   0,   0,   0,   0],
[  0, 0.5,   0, 0.5,   0,   0,   0,   0],
[  0, 0.5,   0,-0.5,   0,   0,   0,   0],
[  0,   0,   0,   0,   1,   0,   0,   0],
[  0,   0,   0,   0,   0,   1,   0,   0],
[  0,   0,   0,   0,   0,   0,   1,   0],
[  0,   0,   0,   0,   0,   0,   0,   1],
]
m3=[
[0.5, 0.5,   0,   0,   0,   0,   0,   0],
[0.5,-0.5,   0,   0,   0,   0,   0,   0],
[  0,   0,   1,   0,   0,   0,   0,   0],
[  0,   0,   0,   1,   0,   0,   0,   0],
[  0,   0,   0,   0,   1,   0,   0,   0],
[  0,   0,   0,   0,   0,   1,   0,   0],
[  0,   0,   0,   0,   0,   0,   1,   0],
[  0,   0,   0,   0,   0,   0,   0,   1],
]

data = [[64,2,3,61,60,6,7,57],
[9,55,54,12,13,51,50,16],
[17,47,46,20,21,43,42,24],
[40,26,27,37,36,30,31,33],
[32,34,35,29,28,38,39,25],
[41,23,22,44,45,19,18,48],
[49,15,14,52,53,11,10,56],
[8,58,59,5,4,62,63,1]]
data2 = data.copy()

for r in range(len(data)):
	last = len(data[r])
	while last >= 2:
		# print(r, last)
		temp = data[r].copy()
		for i in range(int(last/2)):
			temp[i] = (data[r][i*2]+data[r][i*2+1])/2
		for i in range(int(last/2)):
			temp[int(last/2)+i] = (data[r][i*2]-data[r][i*2+1])/2
		print(data[r], temp)
		# input()
		data[r] = temp.copy()
		last /= 2

print(numpy.array(data))

data2 = numpy.dot(data2, m1)
data2 = numpy.dot(data2, m2)
data2 = numpy.dot(data2, m3)
data2 = numpy.dot(numpy.transpose(m1), data2)
data2 = numpy.dot(numpy.transpose(m2), data2)
data2 = numpy.dot(numpy.transpose(m3), data2)
print(data2)

temp = numpy.dot(m1, m2)
temp = numpy.dot(temp, m3)
print(temp)


