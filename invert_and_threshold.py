from PIL import Image
import PIL.ImageOps

def inv_and_thresh(filename):
	savename='Images/'+filename
	def mappoint (i):
	   if i > 80: return 255
	   else: return 0
	PIL_img = Image.open(savename)
	PIL_img = PIL_img.point(mappoint)
	PIL_img = PIL.ImageOps.invert(PIL_img)
	PIL_img.save('Images/INVTHRESH_'+filename)

if __name__=='__main__':
	inv_and_thresh('ball_laplacian_fft_edge.png')
