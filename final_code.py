# Importing OpenCV
import time

import cv2


def train_bg_subtractor(inst, cap, num=500):
    print('Training BG Subtractor...')
    i = 0
    while i < 500:
        _ret, frame = cap.read()
        frame = cv2.resize(frame, (0, 0), None, ratio, ratio)

        fgmask= inst.apply(frame, None, 0.001)
        #cv2.imshow('frame', fgmask)

        i += 1
        if i >= num:
            print('Trained!')


def filter_img(img):
    _, bin_img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)

    # Fill any small holes
    closing = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel)

    # Remove noise
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    # Dilate to merge adjacent blobs
    dilation = cv2.dilate(opening, kernel, iterations=2)

    return dilation


videos = ["surveillance.m4v", "input.mp4", "videoplayback.mp4", "night.mp4", "night2.mp4", "counting.mp4"]
# load the video
cap = cv2.VideoCapture(videos[2])

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

cap = cv2.VideoCapture('input.mp4')

bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500, detectShadows=True)

# skipping 500 frames to train bg subtractor
train_bg_subtractor(bg_subtractor, cap, num=500)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), None, ratio, ratio)
    # convertir a escala de grises
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Filtrado en sal and peper
    median_img = cv2.medianBlur(img, 3)
    # Binarización
    ret, binary_img = cv2.threshold(median_img, 127, 127, cv2.THRESH_BINARY)
    # detección de bordes
    # convolute with proper kernels
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(binary_img, cv2.CV_64F, 1, 0, ksize=5)  # x
    sobely = cv2.Sobel(binary_img, cv2.CV_64F, 0, 1, ksize=5)  # y
    canny_img = cv2.Canny(binary_img, 100, 200)

    # Getting the kernel to be used in Top-Hat
    filterSize = (8, 12)
    """# Elliptical Kernel
    >>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    array([[0, 1],
           [1, 1], dtype=uint8)"""
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)

    # Applying the Top-Hat operation
    tophat_img = cv2.morphologyEx(canny_img,
                                  cv2.MORPH_TOPHAT,
                                  kernel)
    # Applying the Black-Hat operation
    blackhat_img = cv2.morphologyEx(canny_img,
                                    cv2.MORPH_BLACKHAT,
                                    kernel)

    #cv2.imshow('Car Detection System', frame)
    #cv2.imshow('Filtrado', median_img)
    #cv2.imshow('Binarizado', binary_img)
    #cv2.imshow('bordes', canny_img)
    #cv2.imshow('sobelx', sobelx)
    #cv2.imshow('sobely', sobely)


    #cv2.imshow("tophat", tophat_img)
    cv2.imshow("blackhat", blackhat_img)

    fgmask = bg_subtractor.apply(frame, None, 0.001)
    cv2.imshow('Filtered Bin', fgmask)

    if ret:
        filtered_bin_img = filter_img(fgmask)
        time.sleep(0.02)

        contours, hierarchy = cv2.findContours(filtered_bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_contour_area:

                # --------------Tracking---------------
                m = cv2.moments(contour)
                cx = int(m['m10'] / m['m00'])
                cy = int(m['m01'] / m['m00'])
                new = True

                if cy in range(up_limit, down_limit):  # filters out contours that are above line (y starts at top)
                    # x,y is top left corner
                    rect_x, rect_y, rect_width, rect_height = cv2.boundingRect(contour)

                    # creates a rectangle around contour
                    cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (0, 255, 0), 2)

        # show in screen
        cv2.imshow('Filtered Bin', filtered_bin_img)
        cv2.imshow('Frame', frame)
    #cv2.waitKey(5000)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
