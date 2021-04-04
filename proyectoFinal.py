import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageFilter
 
cap=cv2.VideoCapture('trafico.mp4')

while True:
    ret, frame = cap.read()    

    #convertir a escala de grises
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    #Filtrado en sal and peper
    imagentratada = cv2.medianBlur(img, 3)
    #Binarización
    ret,imgbinarizado = cv2.threshold(imagentratada,127,255,cv2.THRESH_BINARY)
    #detección de bordes
    imagen_procesada = cv2.Canny(imgbinarizado,100,200)

    
    cv2.imshow('Car Detection System', img)
    cv2.imshow('Filtrado',imagentratada)
    cv2.imshow('Binarizado', imgbinarizado)
    cv2.imshow('bordes', imagen_procesada)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

