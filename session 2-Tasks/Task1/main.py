import cv2

img=cv2.imread('bear1.jpeg',1)
GrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original pic',img);    cv2.imshow('Gray pic',GrayImg)
cv2.waitKey(0);cv2.destroyAllWindows()
