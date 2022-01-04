# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:36:43 2021

@author: Aaron Ramirez
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

from skimage import filters
from skimage.data import camera
from skimage.util import compare_images
import matplotlib.cm as cm



ruta1 = 'fachada-de-casa.jpg'
image = cv2.imread(ruta1,cv2.IMREAD_GRAYSCALE)


mascara=np.array([[1,1,1],[1,2,1],[1,1,1]])

edge_roberts = filters.roberts(image)
edge_sobel = filters.sobel(image)
edge_prewit= filters.prewitt(image)


fig, axes = plt.subplots(ncols=3, figsize=(6, 4))

axes[0].imshow(edge_roberts, cmap=plt.cm.gray)
axes[0].set_title('Roberts Edge Detection')

axes[1].imshow(edge_sobel, cmap=plt.cm.gray)
axes[1].set_title('Sobel Edge Detection')

axes[2].imshow(edge_prewit,cmap=plt.cm.gray)
axes[2].set_title('Prewit Edge Detecction')



for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()



