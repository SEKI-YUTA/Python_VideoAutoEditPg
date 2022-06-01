import sys
import cv2 as cv
import numpy as np

img = cv.imread("C://Users//yuta//Desktop//autoEditpg//test.jpg")

if img is None:
    sys.exit()
    
cv.imshow("image", img)
k = cv.waitKey(0)
