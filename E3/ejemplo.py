# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 13:02:49 2021

@author: Aaron Ramirez
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.cm as cm

from skimage.util import view_as_blocks




ruta1 = 'fachada-de-casa.jpg'
image = cv2.imread(ruta1,0)
image1= cv2.imread(ruta1)

#####Definir Kernels##############
###Robert###
mRobersX= np.array([[0,0,0],[0,0,1],[0,-1,0]])
mRobersY= np.array([[-1,0,0],[0,1,0],[0,0,0]])

salidax= cv2.filter2D(image,-1,mRobersX)
saliday= cv2.filter2D(image,-1,mRobersY)
imgris= salidax+saliday

view= view_as_blocks(image1,image1.shape)
flat_view = view.reshape(view.shape[0],view.shape[1],-1)
fig, axes= plt.subplots(2,2)
ax=axes.ravel()

ax[0].set_title("imagen en gris"),ax[0].imshow(image,cmap=cm.Greys_r)
ax[1].set_title("sobel x"),ax[1].imshow(salidax,cmap=cm.Greys_r)
ax[2].set_title("sobel y"),ax[2].imshow(saliday,cmap=cm.Greys_r)
ax[3].set_title("sobel x + y"),ax[3].imshow(imgris,cmap=cm.Greys_r)
for a in ax:
    a.set_axis_off()
plt.show()