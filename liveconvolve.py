from SimpleCV import *
from cv import *
from time import time
import numpy as np

# SETUP VARIABLES

wc = CaptureFromCAM(0)
NamedWindow('Camera',CV_WINDOW_AUTOSIZE)
frames = 10 # approximate duration in seconds

# Returns a CvMat object equivalent to entered list matrix
def giveMeCV(l):
	r = cv.CreateMat(len(l),len(l[0]),1)
	for i in range(len(l)):
		for j in range(len(l[0])):
			cv.SetND(r,(i,j),l[i][j])
	return r

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

# Applied Kernel
kernel = sobel

start = time() # for framerate checking (usu. ~30)
for i in range(frames*30):

	# Capture Frame from Webcam
	frame = QueryFrame(wc)
	# Apply Kernel Filter
	Filter2D(frame, frame, kernel)
	# Mirror Image
	Flip(frame,flipMode=1)

	# Display transformed image
	ShowImage('Camera',frame)
	WaitKey(1)
# Frame Rate
print(frames/(time()-start))