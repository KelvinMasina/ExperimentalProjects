import cv2
import easyocr
import pytesseract
from matplotlib import pyplot as plt
import numpy as np
from pytesseract import Output
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Defining the cascade model
haarcascade = "Model/haarcascade_russian_plate_number.xml"

# Read camera
cam = cv2.VideoCapture(1)

# Setting the dimensions of video window
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height

min_area = 500
count = 0

while True:
    success, frame = cam.read()

    plate_cascade = cv2.CascadeClassifier(haarcascade)  # Loading the cascade model
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting image to gray scale

    # Getting number plate coordinates
    plates = plate_cascade.detectMultiScale(frame_gray, 1.1, 7)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

            img_roi = frame[y: y + h, x:x + w]  # Cropping number plate region
            cv2.imshow("ROI", img_roi)


    # Displaying the image
    cv2.imshow("Detecting Plate", frame)
    # Close Camera
    # Saving Image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("SavedPlates/scanned_img" + str(count) + ".jpg", img_roi)
        cv2.rectangle(frame, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", frame)
        cv2.waitKey(500)
        count += 1

    image = cv2.imread("SavedPlates/scanned_img2.jpg")
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

    crop_img_loc = '1.jpg'
    cv2.imshow("Cropped Image", cv2.imread(crop_img_loc))
    cv2.waitKey(0)


    #Ptext = pytesseract.image_to_string(crop_img_loc, lang='eng')
    #print("Number plate is: ", Ptext)
    #cv2.waitKey(0)



    reader = easyocr.Reader(['en'])
    result = reader.readtext(crop_img_loc)
    text = result[0][1]
    print(text)





