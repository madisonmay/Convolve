from PIL import Image
import numpy as np
from numpy import *
from scipy import misc

def convolve_fft(img, kernel):

    #Dimensions of img -- rows/cols
    image_rows, image_cols = img.shape

    fft_img = np.fft.fft2(img, s=(image_rows, image_cols))
    fft_kernel = np.fft.fft2(kernel, s=(image_rows, image_cols))
    fft_image = fft_img * fft_kernel
    print fft_img.shape, fft_kernel.shape, fft_image.shape

    #ignore imaginary components
    # img_out = np.fft.ifft2(fft_image).real
    img_out = np.fft.ifft2(fft_image).real

    return fft_image



# input: image name, 2d kernel
# returns unscaled 3d matrix as well as scaled 3d image matrix
# does fft convolve on each color band and then combines them into one 3d matrix
def convolve_wrapper(imagename, savename):

    #convolution kernel
    kernel = np.matrix([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    img = np.array(Image.open(imagename))

    rows, cols, channels = img.shape
    print rows, cols, channels

    img_r = img[:,:,0]
    img_g = img[:,:,1]
    img_b = img[:,:,2]

    fft_r = convolve_fft(img_r, kernel)
    fft_g = convolve_fft(img_g, kernel)
    fft_b = convolve_fft(img_b, kernel)

    img_out = np.dstack((fft_r,fft_g,fft_b)) #recreating rgb image
    img_unscaled = np.copy(img_out)

    for i in range(channels): #scale each color channel to between 0 and 255
        img_channel = img_out[:,:,i]
        channel_min = img_channel.min()
        img_channel = img_channel- channel_min
        channel_max = img_channel.max()
        img_channel = (img_channel/channel_max)*255.0
        img_out[:,:,i] = img_channel

    img_out = img_out.astype(np.uint8)
    misc.imsave(savename, img_out)
    return img_unscaled, img_out

if __name__ == '__main__':
    convolve_wrapper('lena.png', 'convolved.png')
