import cv2
import numpy as np

# global variables
widthImg = 450
heightImg = 600


# doc scanning functions
def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDil, kernel, iterations=1)
    return imgThres


def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(f'contour area = {area}')
        if area > 5000:
            # cv2.drawContours(imgCont, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(f'perimeter of obj = {peri}')
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            # print(f'figure corners = {objCor}')
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgCont, biggest, -1, (255, 0, 0), 20)
    return biggest


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew


def getWarp(img, biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOut = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    imgCrop = imgOut[20:imgOut.shape[0] - 20, 20:imgOut.shape[1] - 20]
    imgCrop = cv2.resize(imgCrop, (widthImg, heightImg))
    return imgCrop


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# image input
img = cv2.imread("D:\Pictures\doc.jpg")
img = cv2.resize(img, (widthImg, heightImg))
imgCont = img.copy()
imgThres = preProcessing(img)
biggest = getContours(imgThres)
imgWarp = getWarp(img, biggest)
imageArray = ([img, imgCont],
              [imgThres, imgWarp])
stacked = stackImages(0.6, imageArray)
cv2.imshow("image-result", stacked)
cv2.waitKey(0)

# webcam input
'''frame_w = 640
frame_h = 320
cap = cv2.VideoCapture(0)
cap.set(3, frame_w)
cap.set(4, frame_h)
cap.set(10, 150)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (widthImg, heightImg))
    imgCont = img.copy()
    imgThres = preProcessing(img)
    cv2.imshow("image-result",imgThres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
