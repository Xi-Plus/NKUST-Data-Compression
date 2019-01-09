import numpy as np
import cv2


data1 = np.array([
[64,2,3,61,60,6,7,57],
[9,55,54,12,13,51,50,16],
[17,47,46,20,21,43,42,24],
[40,26,27,37,36,30,31,33],
[32,34,35,29,28,38,39,25],
[41,23,22,44,45,19,18,48],
[49,15,14,52,53,11,10,56],
[8,58,59,5,4,62,63,1],
])
data2 = np.array([
[64,2,3,61,60,6,7,57],
[9,55,54,12,13,51,50,16],
[17,47,46,50,50,50,42,24],
[40,26,27,50,50,50,31,33],
[32,34,35,50,50,20,21,43],
[41,23,22,44,45,37,36,30],
[49,15,14,52,53,29,28,38],
[8,58,59,5,4,62,63,1],
])
data2
 = np.array([
[64,2,3,61,60,6,7,57],
[9,12,13,14,13,51,50,16],
[17,15,16,17,21,43,42,24],
[40,18,19,37,55,54,12,33],
[32,34,35,29,47,46,20,25],
[41,23,22,44,26,27,18,48],
[49,15,14,52,53,11,10,56],
[8,58,59,5,4,62,63,1],
])

diff = data1-data2
print(diff)
difflist = np.where(diff != 0)
difflist = list(zip(difflist[0], difflist[1]))

fsize = 2
moves = {}
movescnt = {}

for p1 in difflist:
	for p2 in difflist:
		if p1 != p2:
			if np.array_equal(data1[p1[0]:p1[0]+fsize, p1[1]:p1[1]+fsize], data2[p2[0]:p2[0]+fsize, p2[1]:p2[1]+fsize]):
				dire = tuple(np.array(p2)-np.array(p1))
				if dire not in moves:
					moves[dire] = []
					movescnt[dire] = 0
				moves[dire].append([p1, p2])
				movescnt[dire] += 1

maxdir = max(movescnt.values())
ansmove = list(movescnt.keys())[list(movescnt.values()).index(maxdir)]
print(ansmove)

ansori = np.zeros(data1.shape)
for move in moves[ansmove]:
	ansori[move[0][0]:move[0][0]+fsize, move[0][1]:move[0][1]+fsize] = 1
print(ansori)
