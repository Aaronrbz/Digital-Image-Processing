# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:26:49 2021

@author: Aaron Ramirez
"""

import random
from PIL import Image
import cv2
import numpy as np
def ruido(imagen, porcentaje):

    tamaño=imagen.size[0]*imagen.size[1]
    auxiliar=(tamaño*porcentaje)//800
  
 
    if imagen.mode=='RGB':
       # dato_minimo=(0, 0, 0)
        dato_maximo=(255, 255, 255)
 
    elif imagen.mode=='L':
 #       dato_minimo=0
        dato_maximo=255

    for x in range(auxiliar):
 
        coordenada_x=random.randrange(2, imagen.width-2)
        coordenada_y=random.randrange(2, imagen.height-2)
 
        imagen.putpixel((coordenada_x, coordenada_y), dato_maximo)
        imagen.putpixel((coordenada_x+1, coordenada_y), dato_maximo)
        imagen.putpixel((coordenada_x, coordenada_y+1), dato_maximo)
        imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_maximo)
 

# Escala de grises.
foto=Image.open('prueba1.jpg')
imgGray = foto.convert('L')
imgGray.save('test_gray.jpg')

#llamado a la funcion pasando como parametro la imagen y el
#porcentaje de ruido deseado

bw=Image.open("test_gray.jpg")

ruido(bw, 20)

bw.save('resultadoruido1.jpg')
foto.close()
# mostrar las figuras
img1 = cv2.imread('test_gray.jpg') 
  
img2 = cv2.imread('resultadoruido1.jpg') 
  
  
Hori = np.concatenate((img1, img2), axis=1) 
  
cv2.imshow('Resultado', Hori) 
 

cv2.waitKey(0) 
cv2.destroyAllWindows() 


# Añadir ruido a imagenes con Python
# By  Container: Python's eyes Publisher: Python&#039;s eyes Year: 2017 URL: https://pythoneyes.wordpress.com/2017/06/23/anadir-ruido-a-imagenes-con-python/