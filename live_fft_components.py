from PIL import Image
import numpy as np
from numpy import *
from scipy import misc
import PIL.ImageOps

def convolve_fft(img, kernel, output):

    #Dimensions of img -- rows/cols
    image_rows, image_cols = img.shape


    fft_img = np.fft.fft2(img, s=(image_rows, image_cols))
    fft_kernel = np.fft.fft2(kernel, s=(image_rows, image_cols))
    fft_image = fft_img * fft_kernel
    img_out = np.fft.ifft2(fft_image)

    # fft_img = fft of image, fft_kernel = fft of kernel, fft_image = multiplication of fft_img and fft_kernel, img_out = inverse fft of fft_image
    l = [fft_img, fft_kernel, fft_image, img_out]
    return l[output]



# input: image name, 2d kernel, output
# returns unscaled 3d matrix as well as scaled 3d image matrix
# does fft convolve on each color band and then combines them into one 3d matrix
def convolve_wrapper(imagename, savename, output):

    #convolution kernel
    kernel = np.matrix([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    #img = np.array(Image.open(imagename))
    img = imagename

    rows, cols, channels = img.shape
    #print rows, cols, channels

    img_r = img[:,:,0]
    img_g = img[:,:,1]  
    img_b = img[:,:,2]

    fft_r = convolve_fft(img_r, kernel, output)
    fft_g = convolve_fft(img_g, kernel, output)
    fft_b = convolve_fft(img_b, kernel, output)

    img_out = np.dstack((fft_r,fft_g,fft_b)) #recreating rgb image
    img_unscaled = np.copy(img_out)

    img = abs(255 - img_out[:,:,0]) + abs(255 - img_out[:,:,1]) + abs(255 - img_out[:,:,2])
    #misc.imsave(savename, img.real)

    return img_unscaled, img_out

if __name__ == '__main__':
    ''' 0: fft_img
        1: fft_kernel
        2: fft_image
        3: image_out'''
    convolve_wrapper('Images/'+'miller.jpg', 'Images/'+'fft.png',2)