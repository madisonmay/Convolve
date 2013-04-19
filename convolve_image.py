from __future__ import division
import numpy as np
from scipy import ndimage, misc, signal
from random import randint
from math import floor
from os import system

def convolve_image(img, kernel_str):

    h, w, c = img.shape[0], img.shape[1], img.shape[2]

    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

    # Sobel and Pruitt

    # kernel_str = [1, 0, -1, 1, 0, -1, 1, 0, -1]
    # kernel_str = [1, 0, -1, 2, 0, -2, 1, 0, -1]
    # kernel_str = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    # kernel_str = [-1, -2, -1, 0, 0, 0, 1, 2, 1]

    kernel = np.array([kernel_str[:3],
                       kernel_str[3:6],
                       kernel_str[6:]])

    #rgb photos
    img = r*.2126 + g*.7152 + b*.0722
    img_out = signal.convolve2d(img, kernel, mode='same')

    #normalization
    minimum = np.amin(img_out)
    maximum = np.amax(img_out)
    pixel_range = maximum - minimum
    img_out -= minimum
    img_out = (img_out*255)//pixel_range

    #end result
    return img_out
