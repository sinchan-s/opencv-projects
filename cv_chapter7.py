import cv2

faceCascade = cv2.CascadeClassifier("D:\Pictures\haarcascade_frontalface_default.xml")
img = cv2.imread("D:\Pictures\pp.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
