from SimpleCV import *
from cv import *
from time import time

# SETUP VARIABLES

wc = CaptureFromCAM(0)
NamedWindow('Camera',CV_WINDOW_AUTOSIZE)
frames = 10*30
im_size = (640,480)

channel_img = CreateImage(im_size, IPL_DEPTH_16S, 1)
frame = CreateImage(im_size,8,1)

# FILTER VARIABLES
binary_threshold = 100
laplace_threshold = 5 # must be <31 and odd

start = time()
for i in range(frames):

	frame = QueryFrame(wc)

	# Display transformed image
	ShowImage('Camera',frame)
	WaitKey(1)
print(frames/(time()-start))

	# # Grayscale conversion
	# CvtColor(QueryFrame(wc),frame,CV_RGB2GRAY)
	# #EqualizeHist(frame,frame)

	# # Mirror
	# Flip(frame,flipMode=1)

	# # Apply Binary Threshold (B+W convert)
	# Threshold(frame,frame,binary_threshold,255,CV_THRESH_BINARY)

	# # Apply Laplace Edge Detection
	# Laplace(frame, channel_img,laplace_threshold)
	# Convert(channel_img,frame)