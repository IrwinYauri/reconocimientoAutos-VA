import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageFilter

cap=cv2.VideoCapture('trafico.mp4')

# Object detection from stable camera
object_detector=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=70)

while True:
    ret, frame = cap.read()    
    cv2.imshow('Frame', frame)
  
    #convertir a escala de grises
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    cv2.imshow('Escala de grises', img)
  
    #Filtrado en sal and peper
    imagentratada = cv2.medianBlur(img,3)
    cv2.imshow('Filtro mediana', imagentratada)
    mask=object_detector.apply(imagentratada)
    imagentratada = cv2.medianBlur(mask,3)
  
    #Binarización
    ret,imgbinarizado = cv2.threshold(imagentratada,128,255,cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    imgbinarizado = cv2.dilate(imgbinarizado, kernel, iterations=2)
    cv2.imshow('imgbinarizado', imgbinarizado)
  
    #detección de bordes
    imagen_procesada = cv2.Canny(imgbinarizado,500,1000)
    grad_x = cv2.Sobel(imagen_procesada,cv2.CV_64F,1,0,ksize=5)
    grad_y = cv2.Sobel(imagen_procesada,cv2.CV_64F,0,1,ksize=5)
    
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
        
    sobel = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    #sobel = cv2.add(grad_x, grad_y)
    cv2.imshow('Bordes', sobel)

    #tophat
    rectKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15))
    tophat = cv2.morphologyEx(sobel, cv2.MORPH_TOPHAT, rectKernel)
    #blackhat
    rectKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15))
    blackhat = cv2.morphologyEx(sobel, cv2.MORPH_BLACKHAT, rectKernel)

    imgGrayscalePlusTopHat = cv2.add(img, tophat)
    imgGrayscalePlusTopHatMinusBlackHat = cv2.subtract(imgGrayscalePlusTopHat, blackhat)
    
 
    cv2.imshow('tophat', tophat)
    cv2.imshow('blackhat', blackhat)
    cv2.imshow('imgGrayscalePlusTopHatMinusBlackHat', imgGrayscalePlusTopHatMinusBlackHat)
    
    #aplly mask para reconocer objetos
    #contours = cv2.findContours(cv2.subtract(tophat, blackhat),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours, hierarchy = cv2.findContours(cv2.subtract(tophat, blackhat), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        area = cv2.contourArea(c)
        #print(area)
        hull = cv2.convexHull(c)
        if area > 1300:
            #cv2.drawContours(frame, [hull], 0, (0, 255, 0), 2)
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('Frame', frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

