import cv2
import numpy as np

widthImg = 600
heightImg = 450

frame_w = 640
frame_h = 320
cap = cv2.VideoCapture(0)
cap.set(3, frame_w)
cap.set(4, frame_h)
cap.set(10, 150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDil, kernel, iterations=1)

    return imgThres

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(f'contour area = {area}')
        if area>5000:
            cv2.drawContours(imgCont, cnt, -1, (255, 0, 0), 5)
            peri = cv2.arcLength(cnt, True)
            #print(f'perimeter of obj = {peri}')
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            objCor = len(approx)
            print(f'figure corners = {objCor}')
            if area > maxArea objCor == 4:
                biggest = approx
            x, y, w, h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgCont = img.copy()
    imgThres = preProcessing(img)
    cv2.imshow("image-result",imgThres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
