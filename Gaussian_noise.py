#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:10:56 2021

@author: gillesaye
"""
import numpy as np
import cv2
import os

def add_noise(image):
    #img = cv2.imread(image).astype(np.int8)
    img = cv2.imread('elephant_gray.png').astype(np.int8)
    row, col, ch = img.shape
    mean = 0
    target_noise = 10 ** (35 / 10)
    gauss_noise = np.random.normal(mean, np.sqrt(target_noise), (row,col,ch)).astype(np.int8)

    # Implements a clipping function so pixel values don't roll over (e.g. 253 + 10 = 255)
    noisy = cv2.add(img, gauss_noise)

    # Does not use clipping (e.g (253 + 10) % 255 = 8)
    #noisy = img + gauss_noise
    # noisy = img + gauss_noise

    # Optional preview vs post view for each picture
    cv2.imshow("img", img)
    # cv2.imshow("img", img)
    # cv2.imshow("noisy", noisy) 
    cv2.imshow("noisy", noisy)
    # cv2.waitKey(0)
    cv2.waitKey(0)

    img_name = f"noisey/{image.split('.')[0]}_noisey.png"
    cv2.imwrite(img_name, noisy)
    
def denoise(image):
    
    img2 = cv2.imread('elephant_gray_noisey.png')
    dst = cv2.fastNlMeansDenoisingColored(img2,None,10,10,7,21)
    
    cv2.imshow("denoised", dst)
    

if __name__ == "__main__":
    all_img = [f for f in os.listdir(os.curdir) if os.path.isfile(f) and ".png" in f]

    os.makedirs(os.path.join(os.curdir, 'noisey'), exist_ok=True)

    for i in all_img:
        add_noise(i)
        denoise(i)