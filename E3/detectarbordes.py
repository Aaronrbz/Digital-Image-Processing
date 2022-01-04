# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:24:51 2021

@author: Aaron Ramirez
"""

import matplotlib.pyplot as plt
import cv2
import matplotlib.cm as cm
import numpy as np
import random




def detect_border(imagen,kernelx,kernely,tipo):
    image = cv2.imread(imagen,0)
    image1 = cv2.cvtColor(cv2.imread(imagen),cv2.COLOR_BGR2RGB)
    
    salidax= cv2.filter2D(image,-1,kernelx)
    saliday= cv2.filter2D(image,-1,kernely)
    
    imgris= salidax+saliday

    fig, axes= plt.subplots(2,3)
    ax=axes.ravel()
    
    ax[0].set_title("imagen en gris"),ax[0].imshow(image,cmap=cm.Greys_r)
    ax[1].set_title(tipo+" x"),ax[1].imshow(salidax,cmap=cm.Greys_r)
    ax[2].set_title(tipo + " y"),ax[2].imshow(saliday,cmap=cm.Greys_r)
    ax[3].set_title(tipo +" x + y"),ax[3].imshow(imgris,cmap=cm.Greys_r)
    ax[4].set_title("Imagen Original"),ax[4].imshow(image1,cmap=cm.Greys_r)
    for a in ax:
        a.set_axis_off()
    plt.show()
   
    
    
def sp_noise(image,prob):

    '''
         Agregue ruido de sal y pimienta
         problema: relación de ruido
    '''

    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]

    return output

def mascara(A):
    if(A>0):
        mask= np.ones([3,3])
        mask*= -1
        mask[1,1]=A+8
    if (A<1):
        mask= np.ones([3,3])
        mask[1,1]=A-8
    return mask

def mascara2(A):
    if(A>0):
        mask= np.zeros([3,3])
        mask[1,1]=A+4
        mask[0,1]=-1
        mask[1,0]=-1
        mask[1,2]=-1
        mask[2,1]=-1
    if (A<1):
        mask= np.zeros([3,3])
        mask[1,1]=A-4
        mask[0,1]=1
        mask[1,0]=1
        mask[1,2]=1
        mask[2,1]=1
    return mask

def hig_bost(imagen,mascara,A):
    image = cv2.imread(imagen, 0)
    image1 = cv2.cvtColor(cv2.imread(imagen), cv2.COLOR_BGR2RGB)

    salidax = cv2.filter2D(image1, -1, mascara)


   # view = view_as_blocks(image1, image1.shape)
    #flat_view = view.reshape(view.shape[0], view.shape[1], -1)
    fig, axes = plt.subplots(1, 3)
    ax = axes.ravel()

    ax[0].set_title("imagen en gris"), ax[0].imshow(image, cmap=cm.Greys_r)
    ax[1].set_title("Mejorada Mascara " + A), ax[1].imshow(salidax, cmap=cm.Greys_r)
    ax[2].set_title("Imagen Original"), ax[2].imshow(image1, cmap=cm.Greys_r)
    for a in ax:
        a.set_axis_off()

    plt.show()