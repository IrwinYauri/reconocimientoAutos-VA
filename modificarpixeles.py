from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
#img = mpimg.imread('gato.jpg')
img = np.array(Image.open('conejo.jpg'))

img.setflags(write=1)
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B

cv2.imwrite('negro100.jpg', imgGray)
plt.imshow(imgGray,cmap='gray')

#plt.savefig('gato10.jpg', bbox_inches='tight', pad_inches=0)
#plt.show()

#plt.subplot(1,1,1),plt.imshow(imgGray,cmap='gray')
#plt.title(titles[i])
plt.xticks([]),plt.yticks([])
plt.savefig('conejo20.jpg', bbox_inches='tight', pad_inches=-0.05)
plt.show()

#print("===> ",img.item(10,10,2))
#img.itemset((10,10,2),100)
#print("===> ",img.item(10,10,2))
#====================================================
#img[:,:,2]=img[:,:,2]*0.1140
#plt.imshow(img,vmin=0,vmax=255)
#====================================================
print("------------------------------")

print(img.shape)
print (img.size)
print (img.dtype)