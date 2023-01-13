import cv2

import numpy as np

#To join 2 images , both images size should have same dimensions

img1 = cv2.imread('art1.jpg')
img2 = cv2.imread('art2.jpg')

print(img1.shape)
print(img2.shape)

img3 = cv2.resize(img2, (223,226))


# Horizontal stack
horizontal = np.hstack((img1, img3))
cv2.imshow('horizontal',horizontal )

# Vertical stack
vertical = np.vstack((img1, img3))
cv2.imshow('vertical',vertical)

cv2.waitKey(0)




#_____________________ General Function for Stacking Images____________________

import cv2
import numpy as np


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
     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
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

img1 = cv2.imread('art1.jpg')
img1Gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('art2.jpg')
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#Horizontal
imagStack= stackImages(1,([img1,img2,img1Gray,img2,img2Gray,img1]))
#Vertical
imagStack2= stackImages(1,([img1,img2,img1Gray],[img2,img2Gray,img1]))

cv2.imshow('StackImage', imagStack)
cv2.imshow('StackImage2', imagStack2)
cv2.waitKey(0)

