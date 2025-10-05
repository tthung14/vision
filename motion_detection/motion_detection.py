import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# lay background frame
for i in range(10):
  _, frame = cap.read()
frame = cv2.resize(frame, (640, 480))
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (25, 25), 0) # loc nhieu
last_frame = gray

# frame hien tai - last frame de phat hien chuyen dong
while True:
  _, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (25, 25), 0) # loc nhieu
  abc_img = cv2.absdiff(last_frame, gray)
  # 0 - 1 = tran so (bi nhieu anh sang) neu dung abc(0-1) = 1

  last_frame = gray
  _, img_mask = cv2.threshold(abc_img, 30, 255, cv2.THRESH_BINARY) # loc sang

  contours, _ = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # findContours tim duong vien trong anh nhi phan

  for contour in contours:
    if cv2.contourArea(contour) < 900:
      continue

    # ve hinh chu nhat quanh contour
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

  cv2.imshow("window", frame)

  if cv2.waitKey(1) == ord('q'):
    break;