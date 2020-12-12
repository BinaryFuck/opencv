import numpy as np
import cv2 as cv

target = cv.imread("./NLqu1.jpg")
toGray = cv.cvtColor(target, cv.COLOR_BGR2GRAY)
grayToBgr = cv.cvtColor(toGray, cv.COLOR_GRAY2BGR)
vertical = np.vstack((target, grayToBgr))
cv.imshow("Original ", target)
cv.imshow("Concatenate", vertical)
cv.waitKey(0)
