import cv2
import time


t1 = time.time()
# Load some pre-trained data
# face_data = cv2.CascadeClassifier("C:\Users\HP\PycharmProjects\pythonProject\haarcascade_frontalface_default.xml")
face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Now for testing choose anyone picture from your/our gallery
img = cv2.resize(cv2.imread('C:/Users/HP/PycharmProjects/pythonproject/image/images.jpg'),  (600, 400), fx=0.1, fy=0.1)

# Convert your image color in gray-scale
gray_color_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinate = face_data.detectMultiScale(gray_color_img)

# print(face_coordinate)

# Draw rectangle
for face in face_coordinate:
    (x, y, w, h) = face
    cv2.circle(img, (x+int(w/2), y+int(h/2)), int(w/2), (235, 223, 5), 3)

#    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 155, 205), 2)

cv2.imshow('your-chosen-photo', img)
# cv2.imshow('your-chosen-photo', gray_color_img)
t2 = time.time()

print(t2-t1)
cv2.waitKey()