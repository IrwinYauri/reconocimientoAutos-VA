
# Importing OpenCV and numpy
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
# Defining the kernel to be used in Top-Hat
filterSize =(3, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,
                                   filterSize)
  
# Reading the image named 'input.jpg'
input_image = cv2.imread("placa.png")
#input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Applying the Black-Hat operation
tophat_img = cv2.morphologyEx(input_image, 
                              cv2.MORPH_BLACKHAT,
                              kernel)
  
cv2.imshow("original", input_image)
cv2.imshow("tophat", tophat_img)
cv2.waitKey(5000)
plt.imshow(tophat_img,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.savefig('carro5.jpg', bbox_inches='tight', pad_inches=-0.05,dpi=100)
plt.show()