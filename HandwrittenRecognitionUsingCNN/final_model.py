# Prediction of image drawn in paint
import joblib
import cv2
import numpy as np
import time
import pyscreenshot as imagegrab

model = joblib.load("model/digit_recognizer")
images_folder = "img/"

while True:
    img = imagegrab.grab(bbox=(100, 300, 950, 1000)) # x1, y1, x2, y2
    img.save(images_folder + "img.png")
    image = cv2.imread(images_folder + "img.png")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.GaussianBlur(image_gray, (15, 15), 0)

    # Threshold the Image
    ret , image_threshold = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY)
    roi = cv2.resize(image_threshold, (28, 28), interpolation = cv2.INTER_AREA)
    rows, columns = roi.shape

    X = list()

    # Adding pixel one by one into data array
    for i in range(rows):
        for j in range(columns):
            k = roi[i, j]
            k = 1 if k > 100 else 0
            X.append(k)
    
    predictions = model.predict([X])
    print("Prediction of the number is : ", predictions[0])
    cv2.putText(image, "The Prediction is : " + str(predictions[0]), (20, 20), 0, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.startWindowThread()
    cv2.namedWindow("Result")
    cv2.imshow("Result", image)
    cv2.waitKey(10000)
    if cv2.waitKey(1) == 13 or cv2.waitKey(1) == 27: # 13 is the ascii value of 'enter' and 27 is the ascii value of 'esc'
        break
cv2.destroyAllWindows()