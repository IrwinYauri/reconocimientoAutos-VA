from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

#img = mpimg.imread('gato.jpg')
img = np.array(Image.open('prueba.jpg'))

img.setflags(write=1)

#arr=[[0,50,100,150,200,250],[250,200,150,100,50,0],[0,50,100,150,200,250],[250,200,150,100,50,0],[0,50,100,150,200,250],[250,200,150,100,50,0],[0,50,100,150,200,250],[250,200,150,100,50,0]]
#plt.imshow(arr,cmap='gray')
#plt.show()

#print(img[0,1139])
#print("===> ",img.item(10,10,2))
#img.itemset((10,10,2),100)
#print("===> ",img.item(10,10,2))
#====================================================
#img[:,:,2]=img[:,:,2]*0.1140
#plt.imshow(img,vmin=0,vmax=255)
#====================================================
print("------------------------------")
print("alto: ",img.shape[0])
print("ancho: ",img.shape[1])
print (img.size)
print (img.dtype)


imagentratada=[]

for i in range(img.shape[0]-3):
    row=[]
    for j in range(img.shape[1]-3):
        ventana=[img[i,j],img[i,j+1],img[i,j+2],img[i+1,j],img[i+1,j+1],img[i+1,j+2],img[i+2,j],img[i+2,j+1],img[i+2,j+2]]
        row.append(np.median(ventana))
    imagentratada.append(row)

#print(imagentratada)
plt.imshow(imagentratada,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.savefig('sinsalpimienta.jpg', bbox_inches='tight', pad_inches=-0.05,dpi=100)
plt.show()

