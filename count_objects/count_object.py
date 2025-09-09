import numpy as np
import cv2           # lib OpenCV

VIDEO_USE = False

# ham event khong lam gi trackbar
def nothing(x):
  pass

if VIDEO_USE:
  cap = cv2.VideoCapture(1)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("HMin", "Trackbars", 0, 179, nothing)   # Hue (H): mau sac
cv2.createTrackbar("HMax", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("SMin", "Trackbars", 0, 255, nothing)   # Saturation (S): do bao hoa
cv2.createTrackbar("SMax", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("VMin", "Trackbars", 0, 255, nothing)   # Value (V): do sang
cv2.createTrackbar("VMax", "Trackbars", 255, 255, nothing)

while True:
  if VIDEO_USE:
    ret, frame = cap.read() # doc anh vao bien frame, ret la bien return xem co doc duoc 
    if not ret:
      break
  else:
    frame = cv2.imread(r'D:\python_project\vision_project\images\circle.png')

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # chuyen khong gian mau tu BGR sang HSV

  # keo den lay anh mau dong xu
  h_min = cv2.getTrackbarPos("HMin", "Trackbars")
  h_max = cv2.getTrackbarPos("HMax", "Trackbars")
  s_min = cv2.getTrackbarPos("SMin", "Trackbars")
  s_max = cv2.getTrackbarPos("SMax", "Trackbars")
  v_min = cv2.getTrackbarPos("VMin", "Trackbars")
  v_max = cv2.getTrackbarPos("VMax", "Trackbars")

  lower_bound = np.array([h_min, s_min, v_min])
  upper_bound = np.array([h_max, s_max, v_max])

  mask = cv2.inRange(hsv, lower_bound, upper_bound) # nhung anh dong xu hsv nam trong khoang lower den upper thi la mau trang
  contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # contour la ham tim duong vien

  coin_count = 0
  for contour in contours:
    if cv2.contourArea(contour) > 1000: # tim nhung contour co vung > 1000
    # tim hinh tron
      (x, y, w, h) = cv2.boundingRect(contour) # phat hien cac thong so w h
      aspect_radio = float(w) / h
      if 0.8 <= aspect_radio <= 1.2:
        coin_count += 1
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # ve hinh chu nhat bao quanh dong xu
  cv2.putText(frame, f"Coins: {coin_count}", (10, 50), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255, 0), 2)

  cv2.imshow("Frame", frame)
  cv2.imshow("Mask", mask)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

if VIDEO_USE:
  cap.release()
  
cv2.destroyWindow()