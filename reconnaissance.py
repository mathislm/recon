from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2
import time


def convolve(image, kernel):
    #filtre de sobel
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    pad = int((kW - 1) / 2)
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,cv2.BORDER_CONSTANT, 255)

    output = np.zeros((iH, iW), dtype="float32")

    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # extract the ROI of the image by extracting the
            # *center* region of the current (x, y)-coordinates
            # dimensions
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            # perform the actual convolution by taking the
            # element-wise multiplicate between the ROI and
            # the kernel, then summing the matrix
            k = (roi * kernel).sum()

            # store the convolved value in the output (x,y)-
            # coordinate of the output image
            output[y - pad, x - pad] = k

    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
    return output

def detect_blocs(seuil):
    #detecte des groupes de courbes dans l'image qui a deja subi un seuil
    h = len(seuil)
    n = len(seuil[0])
    courbes = []
    for i in range(h-1,2,-1):
        for j in range(2,n):
            if seuil[i][j] == 255:
                courbes.append([])
                continuite = True
                k,l = i,j
                while (continuite == True):
                    seuil[k][l] = 0
                    courbes[-1].append((k,l))
                    if seuil[k][l+1] == 255 and k < h and l < n-1:
                        k,l = k,l+1
                    elif seuil[k-1][l+1] == 255 and k < h+1 and l < n-1:
                        k,l = k-1,l+1
                    elif seuil[k-2][l+1] == 255 and k < h+2 and l < n-1: 
                        k,l = k-2,l+1
                    elif seuil[k][l] == 255 and k < h and l < n:
                        k,l = k,l
                    elif seuil[k-1][l] == 255 and k < h+1 and l < n:
                        k,l = k-1,l
                    elif seuil[k-2][l] == 255 and k < h+2 and l < n:
                        k,l = k-2,l
                    else:
                        continuite = False

image = cv2.imread('sail.jpg')
cv2.imshow("original", image)

kernel = np.array((
    [0,0,-1],
    [-1,0,1],
    [1,0,0]), dtype ='int')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
conv = convolve(gray, kernel)
cv2.imshow("Convolution", conv)

seuil = cv2.threshold(conv,127,255,cv2.THRESH_BINARY)[1]
cv2.imshow("Seuil", seuil)



            
