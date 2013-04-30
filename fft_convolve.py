from PIL import Image
import numpy as np
from numpy import *
from scipy import misc
import PIL.ImageOps

def convolve_fft(img, kernel):

    #Dimensions of img -- rows/cols
    image_rows, image_cols = img.shape

    fft_img = np.fft.fft2(img, s=(image_rows, image_cols))

    fft_img = np.roll(fft_img, image_rows/2, axis=0)
    fft_img = np.roll(fft_img, image_cols/2, axis=1)

    fft_kernel = np.fft.fft2(kernel, s=(image_rows, image_cols))

    fft_kernel = np.roll(fft_kernel, image_rows/2, axis=0)
    fft_kernel = np.roll(fft_kernel, image_cols/2, axis=1)

    fft_image = fft_img * fft_kernel
    img_out = np.fft.ifft2(fft_image)

    return fft_img



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


    weights = [.2126, .7152, .0722]
    for i in range(channels): #scale each color channel to between 0 and 255
        img_channel = abs(img_out[:,:,i])
        channel_min = img_channel.min()
        img_channel = img_channel- channel_min
        channel_max = img_channel.max()
        img_channel = (img_channel/channel_max)*255.0
        img_out[:,:,i] = img_channel*weights[i]

    def mappoint (i):
        if i > 0: return 255
        else: return 0

    img = img_out[:,:,0] + img_out[:,:,1] + img_out[:,:,2]
    misc.imsave(savename, img.real)

    img = Image.open('fft.png')
    img = img.point(mappoint)
    img.save('fft.png')

    return img_unscaled, img_out

if __name__ == '__main__':
    convolve_wrapper('cityscape.jpg', 'fft.png')
