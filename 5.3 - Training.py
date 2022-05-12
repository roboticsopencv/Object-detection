import cv2

################################################################
#path = 'Resources/haarcascades/haarcascade_frontalface_default.xml'  # PATH OF THE CASCADE
path = 'Resources/haarcascades/haarcascade_mobile.xml'
cameraNo = 0  # CAMERA NUMBER
# OBJECT NAME TO DISPLAY
objectName = 'MOBILE'
frameWidth = 640  # DISPLAY WIDTH
frameHeight = 480  # DISPLAY HEIGHT
color = (255, 0, 255)
#################################################################


cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)