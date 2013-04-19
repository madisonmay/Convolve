#! /usr/bin/env python

from __future__ import division
from sys import argv
import numpy as np
from scipy import ndimage, misc, signal
from random import randint
from math import floor
from os import system

#Python script for first derivative edge detection
#Kernel size: 3X3
#Note: should generate values and then run image processing
#Checking each value from 0 to n**9 can take prohibitively long

# def base10toN(num, base):
#     converted_string = ""
#     current_num = num
#     if not 1 < base < 37:
#         raise ValueError("Base must be between 1 and 36")
#     if not num:
#         return '0'
#     while current_num:
#         mod = current_num % base
#         current_num = current_num // base
#         converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
#     converted_string = (9 - len(converted_string))*"0" + converted_string
#     return converted_string

# def converted(string, m):
#     """Converts a numeric string containing values 0 to m-1
#     to a sequence centered about 0"""
#     assert(m%2 == 1)
#     offset = int(floor(m/2))
#     return [int(c) - offset for c in string]

# def check_combinations(n, value):
#     #now very slow in comparison to generate_combinations
#     #deprecated

#     #for displaying percentage done
#     previous = ''

#     #checking all possibilities with range n
#     result = []
#     end = n**(9)
#     for i in range(1, end):

#         kernel_str = base10toN(i, n)
#         kernel_str = converted(kernel_str, n)

#         #fancy percentage completed output
#         current = str((i/end) * 100)[:2]
#         if current != previous:
#             previous = current
#             if current[1] == '.':
#                 current += '0'
#             # system('clear')
#             print current, "%"



#         #checking for symmetry
#         if not ((kernel_str[:4] == kernel_str[5:][::-1]) and (kernel_str[0] == kernel_str[2]) and (kernel_str[1] == kernel_str[3])):
#             continue

#         #checking for blur -- if
#         if (kernel_str[0] != 0) and (kernel_str[1] != 0) and kernel_str[0]/abs(kernel_str[0]) == -1*kernel_str[1]/abs(kernel_str[1]):
#             #skip photo if blurry
#             continue

#         kernel = np.array([kernel_str[:3],
#                            kernel_str[3:6],
#                            kernel_str[6:]])

#         if sum(kernel_str) != value:
#             kernel[1][1] += (value - sum(kernel_str))
#             kernel_str[4] = kernel[1][1]

#         result.append((kernel_str, kernel))

#     return result

def generate_combinations(n, value):
    result = []
    offset = int(floor(n/2))
    for i in range(0-offset, n-offset):
        for j in range(0-offset, n-offset):
            if (i != 0) and (j != 0) and i/abs(i) == -1*j/abs(j):
                continue
            k = value - 4*i - 4*j
            kernel_str = [i, j, i, j, k, j, i, j, i]
            kernel = np.array([kernel_str[:3],
                               kernel_str[3:6],
                               kernel_str[6:]])
            result.append((kernel_str, kernel))

    for i in range(0-offset, n-offset):
        #horizontal edge detection
        kernel_str = [i, i, i, 0, value, 0, -i, -i, -i]
        kernel = np.array([kernel_str[:3],
                   kernel_str[3:6],
                   kernel_str[6:]])
        result.append((kernel_str, kernel))

        #vertical edge detection
        kernel_str = [i, 0, -i, i, value, -i, i, 0, -i]
        kernel = np.array([kernel_str[:3],
                   kernel_str[3:6],
                   kernel_str[6:]])
        result.append((kernel_str, kernel))

    return result


def all_combinations(file_string, n=3, value=0):
    if (n%2 != 1):
        raise ValueError("The value n must be odd so the distribution can be centered at 0")

    #read image and image properties
    img = misc.imread(file_string, flatten=0)
    h, w, c = img.shape[0], img.shape[1], img.shape[2]

    #checking if img is rgb or greyscale
    if c == 3:
        r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

    #file naming conventions
    folder = file_string.split('.')[0] + '_out_' + str(value)
    image_name = file_string.split('.')[0]

    system('mkdir out')
    system('mkdir out/' + image_name)
    system('clear')
    print('Processing...')

    kernels = generate_combinations(n, value)

    # Sobel Pruitt

    # kernel_str = [1, 0, -1, 1, 0, -1, 1, 0, -1]
    # kernel_str = [1, 0, -1, 2, 0, -2, 1, 0, -1]
    # kernel_str = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    # kernel_str = [-1, -2, -1, 0, 0, 0, 1, 2, 1]

    # kernel = np.array([kernel_str[:3],
    #                kernel_str[3:6],
    #                kernel_str[6:]])
    # kernels = [(kernel_str, kernel)]

    for kernel_str, kernel in kernels:

        #rgb photos
        if c == 3:

            # r2 = signal.convolve2d(r, kernel, mode='same')
            # g2 = signal.convolve2d(g, kernel, mode='same')
            # b2 = signal.convolve2d(b, kernel, mode='same')
            # img_out = np.ndarray(shape=(h, w, c), dtype=int)

            # #combine rgb channels
            # img_out[:,:,0], img_out[:,:,1], img_out[:,:,2] = r2, g2, b2
            img = r*.2126 + g*.7152 + b*.0722
            img_out = signal.convolve2d(img, kernel, mode='same')

        #greyscale
        else:
            img_out = signal.convolve2d(img, kernel, mode='same')

        # #normalization
        minimum = np.amin(img_out)
        maximum = np.amax(img_out)
        pixel_range = (maximum - minimum)/2
        img_out -= minimum
        img_out = (img_out)//pixel_range * 255

        #end result
        kernel_str = '_'.join([str(x) for x in kernel_str])
        misc.imsave('out/' + image_name + '/' + kernel_str + '.jpg', img_out)

    system('rm out/' + image_name + '/' + '0_0_0_0_0_0_0_0_0.jpg')

if __name__ == '__main__':
    all_combinations('lena.png', n=5)
    print "Complete!"
