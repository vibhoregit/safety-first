import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(2)

if vc.isOpened(): # try to get the first frame
	rval, frame = vc.read()
	
else:
	rval = False

while rval:
	#frame2 = cv2.Canny(frame[64:128,:,2],100,200)
	frame3 = cv2.Sobel(frame[64:128,:,2],cv2.CV_8U,0,1,ksize=5)
	#cv2.imshow("preview", frame[64:128,:,2])
	cv2.imshow("preview", frame3)
	rval, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27: # exit on ESC
		break
cv2.destroyWindow("preview")
