#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:03:10 2019

@author: jude
"""
import glob
import cv2
from time import time

MAIN_PATH = '/home/jude/Documents/artem/dev/NAFAA/'
SOUPLESSE_PIC_PATH = MAIN_PATH + 'Souplesse/'

WINDOWS_NAME = 'souplesse'
STRECH_TIME = 5

img_list = glob.glob(SOUPLESSE_PIC_PATH+'*.JPG')

img = cv2.imread(img_list[0])

cv2.namedWindow(WINDOWS_NAME)

i = 0
t = time()
pause = False
streching = False

while True:
    img = cv2.imread(img_list[i])
    if not pause: timer = int(time() - t)

    if timer > STRECH_TIME:
        t = time()
        if i < len(img_list) - 1 : 
            i += 1
        
    cv2.putText(img, str(timer), (10,75), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 5)        
    cv2.imshow(WINDOWS_NAME,img)
    
    K = cv2.waitKey(1) & 0xFF
    if K == ord('q'):
        cv2.destroyAllWindows()
        break
    elif K == ord('n'):
        if i < len(img_list) - 1 : 
            i += 1
            t = time()
    elif K == ord('b'):
        if i > 0 : 
            i -= 1
            t = time()
    elif K == ord('p'):
        pause = not pause
        t = time() - timer


