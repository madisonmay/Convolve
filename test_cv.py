import cv

wc = cv.CaptureFromCAM(0)
cv.NamedWindow('Camera',cv.CV_WINDOW_AUTOSIZE)

while True:
	frame = cv.QueryFrame(wc)
	cv.ShowImage('Camera',frame)
	cv.Flip(frame,flipMode=1)
	test = cv.GetMat(frame)
	cv.DFT(test,test,cv.CV_DXT_FORWARD)
	cv.WaitKey(1)