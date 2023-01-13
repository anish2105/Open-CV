#Function1: Converting Color of the image
import cv2
img = cv2.imread('girl.jpeg')
imgray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray' , imgray)

cv2.waitKey(0)


#Function2: Image Detection Techniques

import cv2
img = cv2.imread('girl.jpeg')
imgray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img , (7,7),0)
cv2.imshow('Blur', imgBlur)
cv2.waitKey(0)

#Function3 : Edge Detetction

import cv2
img = cv2.imread('girl.jpeg')
imgray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img , (7,7),0)
imgCanny = cv2.Canny(img , 100,100)
cv2.imshow('Canny' , imgCanny)
cv2.waitKey(0)

#Function4: Dilation and Erode
# Dilation makes edges thicker
# Erode makes edges thinner

import cv2
import numpy as np
img = cv2.imread('girl.jpeg')
kernel = np.ones((5,5),np.uint8)
imgray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img , (7,7),0)
imgCanny = cv2.Canny(img , 100,100)
imgDilation = cv2.dilate(img , kernel , iterations = 1)
imgerode = cv2.erode(img , kernel , iterations = 1)
cv2.imshow('Dilation ' , imgDilation )
cv2.imshow('Erode ' , imgerode )
cv2.waitKey(0)
