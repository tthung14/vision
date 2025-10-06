import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

face_detection = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # file phat hien khuon mat

face_id = input('\nEnter face Id: ')

print('\n [INFOR] Camera Init ...')

count = 0

while(True):
    ret, img = cam.read()
    img = cv2.flip(img, 1) # 0: lật theo trục X (lật dọc, lên–xuống), 1: lật theo trục Y (lật ngang, trái–phải), -1: lật cả theo trục X và Y (xoay 180)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.3, 5) # tra ve list hinh chu nhat x, y, w, h toa do goc trai khuon mat

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        cv2.imwrite("dataset/User_" + str(face_id) + '_' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27: # nhan ESC
        break
    elif count >= 30:
        break

print("\n [INFOR] Exit")
cam.release()
cv2.destroyAllWindows()