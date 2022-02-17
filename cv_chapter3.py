import cv2
import numpy as np

img = cv2.imread("D:\Pictures\coding.jpg")  # size is quite big so its resized
imgResize = cv2.resize(img, (1000,700))

width, height = 350, 250
pts1 = np.float32([[841, 905], [1905, 961], [785, 1465], [2033, 1505]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("image", imgResize)
cv2.imshow("image-out", imgOut)

cv2.waitKey(0)