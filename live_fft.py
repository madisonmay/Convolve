import cv
import cv2
import numpy as np
import live_fft_components as lfc
from PIL import Image

wc = cv.CaptureFromCAM(0)
cv.NamedWindow('Camera',cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('Magic', cv.CV_WINDOW_AUTOSIZE)

def do_things():
	# Capture Frame from Webcam
	grabbed_frame = cv.QueryFrame(wc)
	frame = grabbed_frame
	# Mirror Image
	cv.Flip(frame,flipMode=1)
	#Numpy Magic
	numframe = np.asarray(frame[:,:])
	[im_unscaled, im_out] = lfc.convolve_wrapper(numframe,'unused',1)
	new_out = np.zeros((im_out.shape[0], im_out.shape[1]))
	new_out[:,:] = im_out[:,:,0]
	print("THIS IS THE TYPE OF IM_OUT")
	print(type(im_out))
	print(im_out.shape)
	current = cv.fromarray(new_out)

	# Display transformed image
	cv.ShowImage('Magic', current)
	# Display captured image
	cv.ShowImage('Camera', grabbed_frame)
	cv.WaitKey(1)
while True:
	do_things()