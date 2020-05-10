import cv2
import numpy as np

def nothing(x):
    pass

file = open('temp.txt', 'r')
name = ''
for i in file:
    name = i.strip()

img = cv2.imread(name,0)
img1 = np.zeros((300, 700, 3), np.uint8)
cv2.namedWindow('Image')

cv2.createTrackbar('Minimum', 'Image', 0, 255, nothing)
cv2.createTrackbar('Maximum', 'Image', 0, 255, nothing)

while(1):
    cv2.imshow('Image', img1)
    cmin = cv2.getTrackbarPos('Minimum', 'Image')
    cmax = cv2.getTrackbarPos('Maximum', 'Image')
    edge = cv2.Canny(img, cmin, cmax)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    else:
        cv2.imshow('Original', img)
        cv2.imshow('Final', edge)

cv2.destroyAllWindows()
