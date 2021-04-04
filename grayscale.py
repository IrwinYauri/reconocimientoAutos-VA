from PIL import Image

img = Image.open('gato.jpg')
imgGray = img.convert('L')
imgGray.save('resultado.jpg')