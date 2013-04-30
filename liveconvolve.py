import cv
from cv import *
from time import time
import numpy as np
from random_kernel import random_kernel

# SETUP VARIABLES

wc = cv.CaptureFromCAM(0)
cv.NamedWindow('Camera',cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('Kernel',cv.CV_WINDOW_AUTOSIZE)
dur = 10000 # approximate duration in seconds

# Returns a CvMat object equivalent to entered list matrix
def giveMeCV(l):
	r = cv.CreateMat(len(l),len(l[0]),1)
	for i in range(len(l)):
		for j in range(len(l[0])):
			cv.SetND(r,(i,j),l[i][j])
	return r

def NumpyToCV(n):
	pass

def CVToNumpy(c):
	pass

# Example Kernels for Testing

sobel = giveMeCV([[-1, 0, 1],
			  	  [-2, 0, 2],
			   	  [-1, 0, 1]])
test = np.matrix([[-1, 0, 1],
				  [-2, 0, 2],
			   	  [-1, 0, 1]])
test = np.transpose(test)
sobelT = giveMeCV(test.tolist())

laplace = giveMeCV([[-1,-1,-1],
					[-1, 8,-1],
					[-1,-1,-1]])

uberlaplace = giveMeCV([[-1,-1,-1,-1,-1],
						[-1,-1,-1,-1,-1],
						[-1,-1,24,-1,-1],
						[-1,-1,-1,-1,-1],
						[-1,-1,-1,-1,-1]])
d = cv.CreateMat(5,5,1)

# Applied Kernel
kernel = laplace

start = time() # for framerate checking (usu. ~30)
for i in range(dur*30):

	# Capture Frame from Webcam
	frame = cv.QueryFrame(wc)
	# Mirror Image
	cv.Flip(frame,flipMode=1)

	# Display raw image
	cv.ShowImage('Camera',frame)

	# Apply Kernel Filter
	kernel = giveMeCV(random_kernel(3,1,0)) # Uncomment for random kernel
	cv.Filter2D(frame, frame, kernel)
	#cv.Invert(frame, frame)

	# Display transformed image
	cv.ShowImage('Kernel',frame)
	cv.WaitKey(1)
# Frame Rate

print(dur/(time()-start))