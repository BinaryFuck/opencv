import numpy as np
import cv2 as cv

img = np.zeros((500, 500, 3), np.uint8)
img[70:303, 30:35] = 0, 255, 0
img[300: 303, 35:130] = 0, 255, 0
img[70:303, 130:133] = 0, 255, 0

img[70:73, 180:270] = 0, 255, 0
img[70:200, 180:183] = 0, 255, 0
img[200:203, 180:270] = 0, 255, 0
img[200:303, 270:273] = 0, 255, 0
img[303:306, 180:273] = 0, 255, 0






cv.imshow("Blank", img)

cv.waitKey(0)
