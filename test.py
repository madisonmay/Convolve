import cv
import numpy as np
a = np.ones((640,480))
a = np.array([[-1,-1,-1],
			  [-1, 8,-1],
			  [-1,-1,-1]])

ex = cv.CreateMat(3,3,8)
for i in range(3):
	for j in range(3):
		cv.SetND(ex,(i,j),-1)
cv.SetND(ex,(1,1),8)

print(repr(ex))