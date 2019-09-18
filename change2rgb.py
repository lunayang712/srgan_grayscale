# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:28:02 2019

@author: Luna
"""

import cv2
import glob as gb
#replace the path with yours
files_all = gb.glob("/Users/Luna/Desktop/Research/GANtest/datagray/small/*.png")
for file in files_all:
    src = cv2.imread(file,0)
    src_RGB = cv2.cvtColor(src,cv2.COLOR_GRAY2BGR)
    cv2.imwrite(file,src_RGB)

