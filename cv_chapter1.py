import cv2
import numpy as np

img = cv2.imread("D:\Pictures\pp.jpg")
kernel = np.ones((5,5),np.uint8)

#Different
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur1 = cv2.GaussianBlur(imgGray,(1,1),0)
imgBlur2 = cv2.GaussianBlur(imgGray,(3,3),0)
imgBlur3 = cv2.GaussianBlur(imgGray,(5,5),0)
imgBlur4 = cv2.GaussianBlur(imgGray,(7,7),0)
imgBlur5 = cv2.GaussianBlur(imgGray,(9,9),0)
imgCanny = cv2.Canny(img,100,100)
imgCanny2 = cv2.Canny(img,150,200)
imgDilation = cv2.dilate(imgCanny2, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation,kernel, iterations=1)

cv2.imshow("outputGray",imgGray)
cv2.imshow("outputBlur4",imgBlur4)
cv2.imshow("outputCanny",imgCanny)
cv2.imshow("outputCanny2",imgCanny2)
cv2.imshow("outputDilation",imgDilation)
cv2.imshow("outputEroded",imgEroded)

cv2.imshow("outputEroded",imgEroded)
cv2.waitKey(0)


'''
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''