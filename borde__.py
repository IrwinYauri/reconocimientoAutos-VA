from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

#img = mpimg.imread('gato.jpg')
img = np.array(Image.open('sinsalpimienta.jpg'))

img.setflags(write=1)

imagentratada=[]
coeficientes = [0,1,0,1,-4,1,0,1,0]
for i in range(img.shape[0]-3):
    row=[]
    for j in range(img.shape[1]-3):
        ventana=img[i,j]*coeficientes[0]+img[i,j+1]*coeficientes[1]+img[i,j+2]*coeficientes[2]+img[i+1,j]*coeficientes[3]+img[i+1,j+1]*coeficientes[4]+img[i+1,j+2]*coeficientes[5]+img[i+2,j]*coeficientes[6]+img[i+2,j+1]*coeficientes[7]+img[i+2,j+2]*coeficientes[8]
        row.append(ventana)
    imagentratada.append(row)

#print(imagentratada)
plt.imshow(imagentratada,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.savefig('sinsalpimienta_zsxxxx.jpg', bbox_inches='tight', pad_inches=-0.05,dpi=100)
plt.show()

'''
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

#img = mpimg.imread('gato.jpg')
img = np.array(Image.open('sinsalpimienta.jpg'))

img.setflags(write=1)

imagentratada=[]
coeficientes = [0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -1, -2, 16, -2, -1, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0]
for i in range(img.shape[0]-5):
    row=[]
    for j in range(img.shape[1]-5):
        ventana=img[i,j]*coeficientes[0]+img[i,j+1]*coeficientes[1]+img[i,j+2]*coeficientes[2]+img[i,j+3]*coeficientes[3]+img[i,j+4]*coeficientes[4]+img[i+1,j]*coeficientes[5]+img[i+1,j+1]*coeficientes[6]+img[i+1,j+2]*coeficientes[7]+img[i+1,j+3]*coeficientes[8]+img[i+1,j+4]*coeficientes[9]+img[i+2,j]*coeficientes[10]+img[i+2,j+1]*coeficientes[11]+img[i+2,j+2]*coeficientes[12]+img[i+2,j+3]*coeficientes[13]+img[i+2,j+4]*coeficientes[14]+img[i+3,j]*coeficientes[15]+img[i+3,j+1]*coeficientes[16]+img[i+3,j+2]*coeficientes[17]+img[i+3,j+3]*coeficientes[18]+img[i+3,j+4]*coeficientes[19]+img[i+4,j]*coeficientes[20]+img[i+4,j+1]*coeficientes[21]+img[i+4,j+2]*coeficientes[22]+img[i+4,j+3]*coeficientes[23]+img[i+4,j+4]*coeficientes[24]
        row.append(ventana)
    imagentratada.append(row)

#print(imagentratada)
plt.imshow(imagentratada,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.savefig('sinsalpimienta_zsxxxx.jpg', bbox_inches='tight', pad_inches=-0.05,dpi=100)
plt.show()


'''