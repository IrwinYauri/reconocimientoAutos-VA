import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageFilter

cap = cv2.VideoCapture('surveillance.m4v')

# parametros
ratio = 1

width = int(cap.get(3)) * ratio
height = int(cap.get(4)) * ratio
frameArea = height * width

# parámetros a controlar
counting_line_up = int(height * 3.5 / 5)
counting_line_down = int(height * 4 / 5)
max_contour_area = frameArea / 400

up_limit = int(counting_line_up * 5 / 6)
down_limit = int(counting_line_down * 7 / 6)

# Object detection from stable camera
object_detector = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

while True:
    ret, frame = cap.read()

    # convertir a escala de grises
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = object_detector.apply(img)
    # Filtrado en sal and peper
    imagentratada = cv2.medianBlur(mask, 3)
    # Binarización
    ret, imgbinarizado = cv2.threshold(imagentratada, 200, 255, cv2.THRESH_BINARY)

    # Fill any small holes
    # closing = cv2.morphologyEx(imgbinarizado, cv2.MORPH_CLOSE, kernel)
    # Remove noise
    # opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    # detección de bordes
    imagen_procesada = cv2.Canny(imgbinarizado, 500, 1000)
    grad_x = cv2.Sobel(imagen_procesada, cv2.CV_64F, 1, 0, ksize=5)
    grad_y = cv2.Sobel(imagen_procesada, cv2.CV_64F, 0, 1, ksize=5)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    sobel = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    # sobel = cv2.add(grad_x, grad_y)

    # tophat
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    tophat = cv2.morphologyEx(sobel, cv2.MORPH_TOPHAT, rectKernel)

    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    blackhat = cv2.morphologyEx(sobel, cv2.MORPH_BLACKHAT, rectKernel)

    imgGrayscalePlusTopHat = cv2.add(img, tophat)
    imgGrayscalePlusTopHatMinusBlackHat = cv2.subtract(imgGrayscalePlusTopHat, blackhat)
    #img_convertida = cv2.cvtColor(imgGrayscalePlusTopHatMinusBlackHat, cv2.COLOR_GRAY2RGB)
    #cv2.imshow('Gris convertida', img_convertida)
    #img3 = cv2.add(frame,img_convertida)
    #cv2.imshow('img3', img3)

    # Buscamos los contornos de las bolas y los dibujamos en verde
    contours, _ = cv2.findContours(imgGrayscalePlusTopHatMinusBlackHat, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Buscamos el centro de las bolas y lo pintamos en rojo
    for i in contours:
        # Calcular el centro a partir de los momentos
        momentos = cv2.moments(i)
        if momentos['m00'] != 0:
            cx = int(momentos['m10'] / momentos['m00'])
            cy = int(momentos['m01'] / momentos['m00'])
        else:
            cx=0
            cy=0

        # x,y is top left corner
        rect_x, rect_y, rect_width, rect_height = cv2.boundingRect(i)

        # creates a rectangle around contour
        cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (0, 255, 0), 2)

    # Mostramos la imagen final
    cv2.imshow('Final', frame)


    # cv2.imshow('tophat', tophat)
    # cv2.imshow('blackhat', blackhat)
    # cv2.imshow('imgbinarizado', imgbinarizado)
    # cv2.imshow('Frame', frame)
    # cv2.imshow('sobel', sobel)
    #cv2.imshow('imgGrayscalePlusTopHatMinusBlackHat', imgGrayscalePlusTopHatMinusBlackHat)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()