# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 18:45:33 2021

@author: Aaron Ramirez
"""

import numpy as np
import cv2

import detectarbordes as borde

######### Robert ##################
mRobersX= np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
mRobersY= np.array([[-1,0,1],[-2,0,2],[-1,0,1]])




###### Lerr imagen #####
ruta1="arania.jpeg"
image = cv2.imread(ruta1,0)
image1 = cv2.imread(ruta1)

borde.detect_border(ruta1, mRobersX, mRobersY, "Robers")