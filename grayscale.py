from PIL import Image

img = Image.open('culebra.jpg')
imgGray = img.convert('L')
imgGray.save('prueba.jpg')