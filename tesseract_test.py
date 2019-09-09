# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/

from PIL import Image
import pytesseract
import argparse
import cv2
import os

imgPath = "test_img.png"
data = pytesseract.image_to_data(Image.open(imgPath))

cvimg = cv2.imread(imgPath)

lines = data.split('\n');
for i in range(1, len(lines)): # skip the first line (header)
    cols = lines[i].split('\t')

    confidence = int(cols[10])
    if confidence <= 0:
        continue

    left = int(cols[6])
    top = int(cols[7])
    width = int(cols[8])
    height = int(cols[9])

    print(cols)

	#draw dis
    cv2.rectangle(cvimg, (left, top), (left + width, top + height), (100, 100, 100), 1)
    cv2.putText(cvimg, cols[10] + "%", (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
    cv2.putText(cvimg, "\"" + cols[11] + "\"", (left, top + height + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

cv2.imshow("xdxd imshow", cvimg)
cv2.waitKey(0)
