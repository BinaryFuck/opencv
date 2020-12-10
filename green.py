import numpy as np
import cv2 as cv

cap = cv.VideoCapture (0)

while True:
    _, frame = cap.read ()

    hsv = cv.cvtColor (frame, cv.COLOR_BGR2HSV)

    lower_green = np.array ([40, 100, 0])
    upper_green = np.array ([80, 255, 255])

    mask = cv.inRange (hsv, lower_green, upper_green)

    res = cv.bitwise_and (frame, frame, mask=mask)

    cv.imshow("Original", frame)
    cv.imshow("white", mask)
    cv.imshow("green", res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
