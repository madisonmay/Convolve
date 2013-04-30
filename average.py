#! /usr/bin/env python

from os import system
from sys import argv
from scipy import ndimage, misc
from future import division

img_files = argv[1:]
imgs = []
for f in img_files:
    img_arrays.append(misc.imread(f, flatten=0))
result = sum(imgs)/len(imgs)
misc.imsave('averaged.jpg', result)



