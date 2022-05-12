Haar cascade - Existing model - Face detection

import cv2
# Load the cascade
face_cascade = cv2.CascadeClassifier('E:/PyCharmFree/Project_1/Exp
4/haarcascades/haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('E:/PyCharmFree/Project_1/Resources/Face.png')
# Convert into grayscale
frameWidth = 612
frameHeight = 408
img = cv2.resize(img, (frameWidth, frameHeight))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
