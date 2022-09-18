import cv2
import numpy as np

img1=cv2.imread('ball.jpeg',1)
img2=cv2.imread('boat1.jpeg',1)
img3=cv2.imread('cat1.jpeg',1)
img4=cv2.imread('cat2.jpeg',1)

newWidth = int(300)
newHeight = int(200)
newDim = (newWidth, newHeight)

smolImg1=cv2.resize(img1,newDim,interpolation=cv2.INTER_AREA)
smolImg2=cv2.resize(img2,newDim,interpolation=cv2.INTER_AREA)
smolImg3=cv2.resize(img3,newDim,interpolation=cv2.INTER_AREA)
smolImg4=cv2.resize(img4,newDim,interpolation=cv2.INTER_AREA)

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


final_img = concat_tile([[smolImg1,smolImg2],[smolImg3,smolImg4]])

cv2.imshow('2x2',final_img);cv2.waitKey(0);cv2.destroyAllWindows()

