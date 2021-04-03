import cv2
#import numpy as np
#from matplotlib import pyplot as plt
 
img = cv2.imread('gato2.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imwrite('negroq.jpg', thresh1)
