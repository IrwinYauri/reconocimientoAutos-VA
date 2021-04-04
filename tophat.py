# import the necessary packages
import argparse
import cv2
  
# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="Path to the image")
#args = vars(ap.parse_args())
  
# load the image and convert it to grayscale
image = cv2.imread("carro3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# construct a rectangular kernel and 
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
 
# a tophat (also called a "whitehat") operation will enable
# us to find light(bright) regions on a dark background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
 
# show the output images
cv2.imshow("Original", image)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)