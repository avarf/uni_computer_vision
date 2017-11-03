import numpy
import cv2
import matplotlib.pyplot as pyplot

# img = cv2.imread('pexels-photo-449007.jpeg', cv2.IMREAD_GRAYSCALE)
"cv2.IMREAD_GRAYSCALE for grey scale color"
"cv2.IMREAD_COLOR for color"
"cv2.IMREAD_UNCHANGED "

# cv2.imshow('image', img)
# cv2.waitKey(0)
# while (1):
# 	cv2.imshow('image',img)
# 	k = cv2.waitKey(33)
# 	if k==119:
# 		print('w')
# 	elif k==ord('a'):
# 		print('AAA')
# 	elif k==113:
# 		break



# "0 is the number of webcam in our system"
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	sub_reg = frame[50:430, 50:590,:]
	subgray = cv2.cvtColor(frame, sub_reg, cv2.COLOR_BGR2GRAY)
	

	cv2.imshow('frame',frame)
	# cv2.imshow('gray',gray)

	k = cv2.waitKey(33)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	if k == ord('q'):
		break
	elif k == ord('g'):
		cv2.imshow('gray',gray)
	elif k == ord('s'):
		cv2.imshow('gray',subgray)

print(frame.shape)
cap.release()
cv2.destroyAllWindows()