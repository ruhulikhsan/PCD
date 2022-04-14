import cv2 as cv2
import numpy as np

img = cv2.imread("Doraemon.jpg")
cv2.imshow("Original Image", img)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilation = cv2.dilate(img,kernel,iterations=1)
cv2.imshow("Dilasi", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()