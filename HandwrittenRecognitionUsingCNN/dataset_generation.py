# Run this code only 1 time untill the data inside the csv file is generated.
# Dont't run this code again after the generation of the data inside the csv file.
import cv2
import csv
import glob

# Generate Dataset
header = ["Lable"]
for i in range(784):
    header.append("Pixel_" + str(i))

with open('Dataset.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(header)

for label in range(10):
    Dir_List = glob.glob("captured_images/" + str(label) + "/*.png")

    for image_path in Dir_List:
        image = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.GaussianBlur(image_gray, (15, 15), 0)
        roi = cv2.resize(image_gray, (28, 28), interpolation=cv2.INTER_AREA)  # Region of Interest

        data = list()
        data.append(label)
        rows, columns = roi.shape

        # Adding pixels one by one into data array
        for i in range(rows):
            for j in range(columns):
                k = roi[i, j]
                k = 1 if k > 100 else 0
                data.append(k)

        with open('Dataset.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)
