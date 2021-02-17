import cv2 as cv
import rescale

img = cv.imread("images/cat0.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Cat", rescale.rescale(gray_img, 0.25))
cv.waitKey(0)