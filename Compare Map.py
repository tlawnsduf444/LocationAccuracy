import cv2
import numpy as numpy

img = cv2.imread('ddd.png')

blue_cnt = 0
purple_cnt = 0

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img.item(i,j,0) >= 255 and img.item(i,j,2) < 255:
            blue_cnt += 1
        if img.item(i,j,0) <= 200 and img.item(i,j,2) <= 200:
            purple_cnt += 1

percentage = float((purple_cnt/(blue_cnt + purple_cnt)) * 100)
print(percentage)
