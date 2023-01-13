import cv2

print('Imported')

#Step1: reading images

img = cv2.imread('art1.jpg')
#'art' which is the first parameter should be given in imshow as the name of the pic
cv2.imshow('art', img)
#It displays and disappears in milli seconds, so we should add cv2.waitKey() to make it stay for a while
cv2.waitKey(0)
# if We put 0 then until we close the pic window will be open
# if we put any another number, that much amount of time the window will be opened in mili seconds


#Step2 : Streaming vidoes

cap = cv2.VideoCapture('dcvid1.mov')
while True:
    sucess , img = cap.read()
    cv2.imshow('art', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Step3: Streaming from webcam

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10 , 100)
while True:
    sucess , img = cap.read()
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
