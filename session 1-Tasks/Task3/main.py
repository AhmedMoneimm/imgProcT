import numpy as np
import cv2

img=cv2.imread('boat1.jpeg',0)
img[img >=255] = 0  #the required threshold value (manual/static or make a fuction for it to be dynamic)

cv2.imshow('NewImg',img);cv2.waitKey(0);cv2.destroyAllWindows()