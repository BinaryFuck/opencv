import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)
#  Here we are using array built-in function np.zeros to create image of 512 512 width and height and 3 is
# actually to give functionality for giving colors on pic and np.uint8 is used because while giving color
# we have to use RGB values which vary from 0,255 so they all are in integers to for which we specifying

# let Color It Try It With Blue
img[:] = 255, 0, 0
#Try It With Different Colors
# first lets check it
cv.imshow('blank', img)
cv.waitKey(0)

