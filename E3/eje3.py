# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:32:56 2021

@author: Aaron Ramirez
"""

import numpy as np
import cv2

import detectarbordes as borde

######## Sobel  #######

KernelSobelX = np.array([[1,0,-1],[2,0,-2],[1,0,1]])
KernelSobelY = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])



####### Kernel Prewitt ######

KernelPrewiiX =  np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
KernelPrewiiY =  np.array([[1,1,1],[0,0,0],[2,2,2]])


######## Kerne Laplaciano ###########
KernelLaplaceX =  np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
KernelLaplaceY =  np.array([[-1,0,1],[-2,0,2],[-1,0,1]])



###### Lerr imagen #####
ruta1="arania.jpeg"
image = cv2.imread(ruta1,0)
image1 = cv2.imread(ruta1)

borde.detect_border(ruta1,KernelSobelX,KernelSobelY,"Sobel")
borde.detect_border(ruta1,KernelPrewiiX,KernelPrewiiY, "Prewitt ") 
borde.detect_border(ruta1, KernelLaplaceX, KernelLaplaceY, "Laplaciano")