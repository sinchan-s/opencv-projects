import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img2 = np.ones((512, 512, 3), np.uint8)

'''print(img)
img[200:300, 200:300] = 132, 20, 50
img2[:] = 132, 20, 50'''

# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2. circle(img, (400, 50), 30, (200, 111, 0), 5)
cv2.putText(img2, "hey its working", (250, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 110, 110), 1)

cv2.imshow("image", img)
cv2.imshow("image2", img2)

cv2.waitKey(0)
