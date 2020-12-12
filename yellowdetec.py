import numpy as np
import cv2 as cv

target = cv.imread('./sunflower.jpeg')
horizontal_Oignal = np.hstack((target, target))
hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
lower_yellow = np.array([25, 120, 0])
upper_yellow = np.array([40, 255, 255])

yellow_mask = cv.inRange(hsv, lower_yellow, upper_yellow)
yellow_final = cv.bitwise_and(target, target, mask=yellow_mask)
yellow_concat = np.hstack(( yellow_mask, yellow_mask))
cv.imshow("Orignal", target)
cv.imshow("masked", yellow_mask)
cv.imshow("Detected", yellow_final)
cv.imshow("Concat", yellow_concat)

# cv.imshow("Orignal", target)
# cv.imshow("Concat Orignal", horizontal_Oignal)
cv.waitKey(0)
