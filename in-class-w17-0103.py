import numpy as np
import cv2
from bisect import bisect_left


data = np.array([6.2, 9.7, 13.2, 5.9, 8, 7.4, 4.2, 1.8])
print("data", data)
diff = np.diff(np.concatenate((np.array([0]), data)))
print("diff", diff)

quantizer = [-6, -4, -2, 0, 2, 4, 6]
def fqu(quantizer, v):
	idx = bisect_left(quantizer, v)
	if idx >= len(quantizer):
		return quantizer[idx-1]
	if idx == 0:
		return quantizer[0]
	if quantizer[idx] - v <= v - quantizer[idx-1]:
		return quantizer[idx]
	else:
		return quantizer[idx-1]

quantized = []
for v in diff:
	quantized.append(fqu(quantizer, v))

print("quantized", quantized)
reconstruction = np.cumsum(quantized)
print("reconstruction", reconstruction)
print("error", data-reconstruction)
