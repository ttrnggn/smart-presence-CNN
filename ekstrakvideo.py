import cv2
import face_recognition as fr
import os

ctr = 1
for i in range (200):
    path = ('Face/andy/image (%d).jpg' % ctr)
    img = cv2.imread(path)
    face_locations = fr.face_locations(img)
    for face_location in face_locations :
        top, right, bottom, left = face_location
        cropimg = img[top-100:bottom+20, left:right+30]
        cv2.imwrite("Croppedimg/andy/images_%d.jpg" %ctr, cropimg)
    ctr+=1
    print(ctr)