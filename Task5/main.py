import numpy as np; import cv2

img=cv2.imread('wood.jpg',1)
ker=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

newImg=cv2.filter2D(img,-1,ker)
cv2.imshow('Original',img)
cv2.imshow('New',newImg)

cv2.waitKey(0)
cv2.imwrite('AfterApplyingFilter',newImg)
cv2.destroyAllWindows()