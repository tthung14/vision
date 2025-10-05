import cv2
import pytesseract

# download tesseract.exe

READ_VIE = False

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("D:\\python_project\\vision_project\\images\\name_vie.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

if READ_VIE:
    text = pytesseract.image_to_string(img, lang="vie") # nhan dien tieng viet
    print(text)
    with open("dich.txt", "a", encoding="utf-8") as f: # a la ghi noi duoi
        f.writelines(text)

else:
    boxes = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):   # enumerate de lay index cho list (index: x, data: b)
        if x != 0: # bo dong dau tien
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9]) # lay ra toa do x, y, w, h cua text
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2) # ve hinh chu nhat quanh text
                cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 255), 1)
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()