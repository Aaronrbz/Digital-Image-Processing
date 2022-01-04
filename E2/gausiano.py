# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:48:21 2021

@author: Aaron Ramirez
"""

import cv2
#import random
import numpy as np
from matplotlib import pyplot as plt



def gasuss_noise(image, mean=0, var=0.001):

    '''
                 Agregue ruido gaussiano
                 significar: significar
                 var: varianza
    '''
    
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)

    return out

img = cv2.imread("test_gray.jpg")

# Agregue ruido gaussiano con un valor medio de 0 y una varianza de 0.01
out2 = gasuss_noise(img, mean=0, var=0.01)


# Mostrar imagen
titles = ['Original ','Gaussian']
images = [img, out2]

plt.figure(figsize = (20, 15))
for i in range(2):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



