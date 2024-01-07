import cv2
import numpy as np

img = cv2.imread("SolarImage.jpg")

cv2.imshow("resultado",img)

cv2.waitKey(0)

cv2.putText(img, "Sol", (120, 70), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=2, color=(0,150,255))

cv2.putText(img, "Mercurio", (120, 170), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(150,150,150))

cv2.putText(img, "Venus", (180, 150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(100,150,255))

cv2.putText(img, "Terra", (280, 150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,0))

cv2.putText(img, "Marte", (380, 180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(50,150,255))

cv2.putText(img, "Jupiter", (380, 80), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=2, color=(150,190,255))

cv2.putText(img, "Saturno", (680, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=2, color=(100,190,255))

cv2.putText(img, "Urano", (880, 150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1.5, color=(250,200,150))

cv2.putText(img, "Netuno", (1050, 150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1.5, color=(250,150,20))


cv2.imwrite("Solar_systemwithname.jpg",img)