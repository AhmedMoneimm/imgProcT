import cv2
import numpy as np

recVid = cv2.VideoCapture("Shape Detection 1.mp4")


while(1):

	_, imageFrame = recVid.read()

	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

	red_lower = np.array([166, 70, 75], np.uint8)
	red_upper = np.array([180, 255, 210], np.uint8)
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
##############################################################################
	yellow_lower = np.array([22, 93, 0], np.uint8)
	yellow_upper = np.array([45, 255, 255], np.uint8)
	yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

	kernal = np.ones((5, 5), "uint8")
	
	#red
	red_mask = cv2.dilate(red_mask, kernal)
	res_red = cv2.bitwise_and(imageFrame, imageFrame,mask = red_mask)
	
	#yellow
	yellow_mask = cv2.dilate(yellow_mask, kernal)
	res_yellow = cv2.bitwise_and(imageFrame, imageFrame,mask = yellow_mask)
	

	#contours
	contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),(x + w, y + h),(0, 0, 255), 2)
			
			cv2.putText(imageFrame, "red star", (x, y),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(0, 0, 255))	

###########################################################################
	contours, hierarchy = cv2.findContours(yellow_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),(x + w, y + h),(0, 255, 255), 2)
			
			cv2.putText(imageFrame, "yellow box", (x, y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 255))

			
	cv2.imshow("ROV recoreded video", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		recVid.release()
		cv2.destroyAllWindows()
		break
