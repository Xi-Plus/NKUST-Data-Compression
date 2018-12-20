import numpy as np
import cv2


path = "lena256.bmp"
path = "Peppers.bmp"
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

print(img.shape)
height, width = img.shape

def getM(x, y):
	M = np.zeros((x, x))
	for r in range(y // 2):
		M[r * 2    , r         ] = 0.5
		M[r * 2 + 1, r         ] = 0.5
		M[r * 2    , r + y // 2] = 0.5
		M[r * 2 + 1, r + y // 2] = -0.5
	for r in range(y, x):
		M[r, r] = 1
	return M


np.set_printoptions(precision=2, suppress=True)
# np.set_printoptions(threshold=np.inf)
# print(getM(16, 16))
# print(getM(16, 8))
# print(getM(16, 4))
# print(getM(16, 2))
# exit()
data = [[64,2,3,61,60,6,7,57],
[9,55,54,12,13,51,50,16],
[17,47,46,20,21,43,42,24],
[40,26,27,37,36,30,31,33],
[32,34,35,29,28,38,39,25],
[41,23,22,44,45,19,18,48],
[49,15,14,52,53,11,10,56],
[8,58,59,5,4,62,63,1]]
# img=np.array(data)
# height, width = img.shape
print(img)

offset = width
while offset >= 2:
	# print(offset)
	# print(getM(width, offset))
	img = np.dot(img, getM(width, offset))
	offset //= 2

offset = width
while offset >= 2:
	img = np.dot(getM(width, offset).T, img)
	offset //= 2

print(img)

img[(-5 < img) & (img < 5)] = 0

offset = 2
while offset <= width:
	img = np.dot(np.linalg.inv(getM(width, offset).T), img)
	offset *= 2

offset = 2
while offset <= width:
	# print(offset)
	# print(getM(width, offset))
	img = np.dot(img, np.linalg.inv(getM(width, offset)))
	offset *= 2

cv2.imwrite("out.bmp", img)

# data2 = numpy.dot(data2, m1)
# data2 = numpy.dot(data2, m2)
# data2 = numpy.dot(data2, m3)
# data2 = numpy.dot(numpy.transpose(m1), data2)
# data2 = numpy.dot(numpy.transpose(m2), data2)
# data2 = numpy.dot(numpy.transpose(m3), data2)
# print(data2)

# temp = numpy.dot(m1, m2)
# temp = numpy.dot(temp, m3)
# print(temp)


