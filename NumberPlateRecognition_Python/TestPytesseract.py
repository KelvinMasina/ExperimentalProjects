import cv2
import easyocr
import pytesseract
from matplotlib import pyplot as plt
import numpy as np
from pytesseract import Output
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread("SavedPlates/Cars412.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = cv2.bilateralFilter(image_gray, 11, 17, 17)
edged = cv2.Canny(image_gray, 170, 200)

contours, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1 = image.copy()
cv2.drawContours(image1, contours, -1, (0, 255, 0), 3)

contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
NumPlateCount = None

image2 = image.copy()
cv2.drawContours(image2, contours, -1, (0, 255, 0), 3)
cv2.imshow("Top 30 cnts", image2)
cv2.waitKey(0)

count2 = 0
name = 1

for i in contours:
    perimeter = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.02*perimeter, True)

    if (len(approx) == 4):
        NumPlateCount = approx

        x, y, w, h = cv2.boundingRect(i)
        crp_img = image[y:y+h, x:x+w]
        cv2.imwrite(str(name) + '.png', crp_img)
        name += 1

        break

cv2.drawContours(image, [NumPlateCount], -1, (0, 255, 0), 3)
cv2.imshow("Final Image", image)
cv2.waitKey(0)

crop_img_loc = '1.png'
cv2.imshow("Cropped Image", cv2.imread(crop_img_loc))
cv2.waitKey(0)


text = pytesseract.image_to_string(crop_img_loc, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
if len(text) >= 7:
    print("License Plate is: ", text[1:8])


#reader = easyocr.Reader(['en'])
#result = reader.readtext(crop_img_loc)
#text = result
#print("The number plate is ", text)
