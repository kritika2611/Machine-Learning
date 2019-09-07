import cv2

cam=cv2.VideoCapture(0)

while True:
	ret,frame=cam.read()

	if ret==False:       #checking whether frame is available
		print('an error occured')
		continue          #it continues implementing the loop untill it gets a frame
	cv2.imshow("my video",frame)

	key_pressed=cv2.waitKey(1)& 0xFF  #checks every 1ms whether a key is pressed  # 0xFF=masks all the bits expect last 8
	if key_pressed==ord('q'):
		break

cam.release()
cv2.destroyAllWindows()