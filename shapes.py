# import cv2
# import numpy as np
# img = np.zeros((500 , 500))
# img2 = np.zeros((500 , 500 , 3))
# cv2.imshow('zero' , img)
# cv2.imshow('zero2' , img2)
# cv2.waitKey(0)
# print(img.shape)
# print(img2.shape)
#
#
# #------------------------Adding Color------------------------#
#
# import cv2
# import numpy as np
#
# img2 = np.zeros((500 , 500 , 3))
# img3 = np.zeros((500 , 500 , 3))
# img2[:] = 255,0,0  #BGR
# img3[100:450 , 0: 350] = 255,0,0  #BGR
# cv2.imshow('zero2' , img2)
# cv2.imshow('zero3' , img3)
# cv2.waitKey(0)


# #Add lines
#
# import cv2
# import numpy as np
# img3 = np.zeros((500 , 500 , 3))
# img3[100:450 , 0: 350] = 255,0,0  #BGR
# cv2.line(img3 , (0,0) , (250,250) , (0,0,255) ,1 )  #Image_name , start point of the line , end point of the line  , color of line , thickness of line
# cv2.imshow('zero3' , img3)
# cv2.waitKey(0)
#
# #Add Shapes
#
# import cv2
# import numpy as np
# img3 = np.zeros((500 , 500 , 3))
# img3[100:450 , 0: 350] = 255,0,0  #BGR
# cv2.rectangle(img3 , (0,0) , (500,500) , (0,255,0) ,cv2.FILLED )  #Image_name , start point of the line , end point of the line  , color of line , thickness of line
# cv2.imshow('zero3' , img3)
# cv2.waitKey(0)

#Add Text

import cv2
import numpy as np
img = np.zeros((500,500,3))

cv2.circle(img,(250,250),100,(255,0,0),2)
cv2.putText(img,'this is a circle',(150,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
cv2.imshow('image',img)

cv2.waitKey(0)
