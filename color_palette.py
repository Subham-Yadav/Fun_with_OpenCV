import numpy as np
import cv2

def nothing(x):
    pass

img = np.zeros((300, 530, 3), np.uint8)
cv2.namedWindow('Color Palette')


cv2.createTrackbar('R', 'Color Palette', 0, 255, nothing)
cv2.createTrackbar('G', 'Color Palette', 0, 255, nothing)
cv2.createTrackbar('B', 'Color Palette', 0, 255, nothing)

switch = "0 : OFF \n 1 : ON"
cv2.createTrackbar(switch, 'Color Palette', 0, 1, nothing)

  
flag=0
while(1):
    cv2.imshow('Color Palette', img)
    k = cv2.waitKey(50) & 0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R', 'Color Palette')
    g = cv2.getTrackbarPos('G', 'Color Palette')
    b = cv2.getTrackbarPos('B', 'Color Palette')
    s = cv2.getTrackbarPos(switch, 'Color Palette')
    if s == 0:
        img[:] = 0

    else:
        img[:] = [b,g,r]


cv2.destroyAllWindows()
       
