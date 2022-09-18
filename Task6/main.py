import cv2;import numpy as np

img = cv2.imread("fish.jpg") 

#adaptive parameters/arguments
v = np.median(img)
lower = int(max(0, (1.0 - 0.33) * v))      #sigma=0.33
upper = int(min(255, (1.0 + 0.33) * v))

edge = cv2.Canny(img, lower, upper)

cv2.imshow('original', img)
cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.imwrite('Edge',edge)
cv2.destroyAllWindows()
