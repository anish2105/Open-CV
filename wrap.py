import cv2
import numpy as np

img = cv2.imread('card.jpeg')
width,height = 250, 350
pts1 = np.float32([ [234,59] , [343,49] , [255,216] ,[371,203] ])
pts2 = np.float32([ [0,0] , [width,0] , [0,height] , [width , height]  ])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img , matrix , (width , height))
cv2.imshow('card' , img)
cv2.imshow('Wrapped' , output)
cv2.waitKey(0)