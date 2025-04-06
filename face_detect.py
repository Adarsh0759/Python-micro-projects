import cv2 as cv

img=cv.imread('Resources/group.webp')
cv.imshow('Group of 6 people',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade=cv.CascadeClassifier('Python\haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected faces',img)
print(f'Number of faces found={len(faces_rect)}')
cv.waitKey(0)