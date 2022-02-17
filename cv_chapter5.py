import cv2
import numpy as np

def empty():


path = "D:\Pictures\lambo.png"
cv2.namedWindow("TrackBars")
cv2.resize("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)

img = cv2.imread(path)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("image", img)
cv2.imshow("image-hsv", imgHSV)

cv2.waitKey(0)