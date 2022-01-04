# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:57:35 2021

@author: Aaron Ramirez
"""

import imutils as im
import cv2
from skimage.util import random_noise
from skimage import filters
from skimage.morphology import disk
import matplotlib.pyplot as plt
import matplotlib.cm as cm

ruta1 = 'test_gray.jpg'
imagen = cv2.imread(ruta1,cv2.IMREAD_GRAYSCALE)
#Tipos de ruido
imgSalt = random_noise(imagen, mode='salt')
imgPepper = random_noise(imagen, mode='pepper')
imgGaussian1 = random_noise(imagen, mode='gaussian', var = 0.2)
imgGaussian2 = random_noise(imagen, mode='gaussian', var = 1.2)
imgLocalvar = random_noise(imagen, mode='localvar')
imgSp = random_noise(imagen, mode='s&p')


fib, axes = plt.subplots(3, 4)
ax = axes.ravel()
#Salt
ax[0].set_title("Sal")
ax[0].imshow(imgSalt, cmap = cm.Greys_r) 
#Pepper
ax[2].set_title("Pimienta")
ax[2].imshow(imgPepper, cmap = cm.Greys_r) 

#Localvar
ax[4].set_title("Localvar")
ax[4].imshow(imgLocalvar, cmap = cm.Greys_r) 
 
#s&p
ax[6].set_title("Sal y Pimienta")
ax[6].imshow(imgSp, cmap = cm.Greys_r) 

#Gaussian < 1
ax[8].set_title("Gaussian <1")
ax[8].imshow(imgGaussian1, cmap = cm.Greys_r) 
#Gaussian > 1
ax[10].set_title("Gaussian >1")
ax[10].imshow(imgGaussian2, cmap = cm.Greys_r) 

for a in ax:
    a.axis("off")
plt.tight_layout()
plt.show()

