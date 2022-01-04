# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:36:22 2021

@author: Aaron Ramirez
"""
import random
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage

def ruidoSal(imagen, porcentaje):

    tamaño=imagen.size[0]*imagen.size[1]
    auxiliar=(tamaño*porcentaje)//800
  
 
    if imagen.mode=='RGB':
       # dato_minimo=(0, 0, 0)
        dato_maximo=(255, 255, 255)
 
    elif imagen.mode=='L':
 #       dato_minimo=0
        dato_maximo=255
 
    #pixeles blancos
    for x in range(auxiliar):
 
        coordenada_x=random.randrange(2, imagen.width-2)
        coordenada_y=random.randrange(2, imagen.height-2)
 
        imagen.putpixel((coordenada_x, coordenada_y), dato_maximo)
        imagen.putpixel((coordenada_x+1, coordenada_y), dato_maximo)
        imagen.putpixel((coordenada_x, coordenada_y+1), dato_maximo)
        imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_maximo)
 
    #pixeles negros
    # for x in range(auxiliar):
 
    #     coordenada_x=random.randrange(2, imagen.width-2)
    #     coordenada_y=random.randrange(2, imagen.height-2)
 
    #     imagen.putpixel((coordenada_x, coordenada_y), dato_minimo)
    #     imagen.putpixel((coordenada_x+1, coordenada_y), dato_minimo)
    #     imagen.putpixel((coordenada_x, coordenada_y+1), dato_minimo)
    #     imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_minimo)
 
    # return None
def ruidopimienta(imagen, porcentaje):

    tamaño=imagen.size[0]*imagen.size[1]
    auxiliar=(tamaño*porcentaje)//800
  
 
    if imagen.mode=='RGB':
        dato_minimo=(0, 0, 0)
       # dato_maximo=(255, 255, 255)
 
    elif imagen.mode=='L':
        dato_minimo=0
     #   dato_maximo=255
 
    #pixeles blancos
    # for x in range(auxiliar):
 
    #     coordenada_x=random.randrange(2, imagen.width-2)
    #     coordenada_y=random.randrange(2, imagen.height-2)
 
    #     imagen.putpixel((coordenada_x, coordenada_y), dato_maximo)
    #     imagen.putpixel((coordenada_x+1, coordenada_y), dato_maximo)
    #     imagen.putpixel((coordenada_x, coordenada_y+1), dato_maximo)
    #     imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_maximo)
 
   # pixeles negros
    for x in range(auxiliar):
 
        coordenada_x=random.randrange(2, imagen.width-2)
        coordenada_y=random.randrange(2, imagen.height-2)
 
        imagen.putpixel((coordenada_x, coordenada_y), dato_minimo)
        imagen.putpixel((coordenada_x+1, coordenada_y), dato_minimo)
        imagen.putpixel((coordenada_x, coordenada_y+1), dato_minimo)
        imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_minimo)
 
    return None



def ruidosp(imagen, porcentaje):

    tamaño=imagen.size[0]*imagen.size[1]
    auxiliar=(tamaño*porcentaje)//800
  
 
    if imagen.mode=='RGB':
        dato_minimo=(0, 0, 0)
       # dato_maximo=(255, 255, 255)
 
    elif imagen.mode=='L':
        dato_minimo=0
        dato_maximo=255
 
   # pixeles blancos
    for x in range(auxiliar):
 
        coordenada_x=random.randrange(2, imagen.width-2)
        coordenada_y=random.randrange(2, imagen.height-2)
 
        imagen.putpixel((coordenada_x, coordenada_y), dato_maximo)
        imagen.putpixel((coordenada_x+1, coordenada_y), dato_maximo)
        imagen.putpixel((coordenada_x, coordenada_y+1), dato_maximo)
        imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_maximo)
 
    #pixeles negros
    for x in range(auxiliar):
 
        coordenada_x=random.randrange(2, imagen.width-2)
        coordenada_y=random.randrange(2, imagen.height-2)
 
        imagen.putpixel((coordenada_x, coordenada_y), dato_minimo)
        imagen.putpixel((coordenada_x+1, coordenada_y), dato_minimo)
        imagen.putpixel((coordenada_x, coordenada_y+1), dato_minimo)
        imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_minimo)
 
    return None

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
    img = cv2.imread("test_gray.jpg")

   


    return out




bw=Image.open("test_gray.jpg")



# mostrar las figuras
########################################
ruidoSal(bw, 10)
bw.save('resultadoruido2.jpg')  
img1 = cv2.imread('test_gray.jpg') 
  
img2 = cv2.imread('resultadoruido2.jpg') 
  

Hori = np.concatenate((img1, img2), axis=1) 
  
cv2.imshow('Resultado sal al 10', Hori) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

###########################################


ruidopimienta(bw, 30)
bw.save('resultadoruido2.jpg')  
img1 = cv2.imread('test_gray.jpg') 
  
img2 = cv2.imread('resultadoruido2.jpg') 
  

Hori = np.concatenate((img1, img2), axis=1) 
  
cv2.imshow('Resultado pimienta al 30', Hori) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
#############################################

ruidosp(bw, 30)
bw.save('resultadoruido2.jpg')  
img1 = cv2.imread('test_gray.jpg') 
  
img2 = cv2.imread('resultadoruido2.jpg') 
  

Hori = np.concatenate((img1, img2), axis=1) 
cv2.imshow('Resultado S&P al 30%', Hori) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
#########################333

locavar()
#######################
img = cv2.imread("test_gray.jpg")

# Agregue ruido gaussiano con un valor medio de 0 y una varianza de 0.01
out2 = gasuss_noise(img, mean=0.1, var=0.01)


titles = ['Original ','Gaussian']
images = [img, out2]

plt.figure(figsize = (20, 15))
for i in range(2):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
