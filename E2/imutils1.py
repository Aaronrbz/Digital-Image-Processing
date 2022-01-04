# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 13:05:39 2021

@author: Aaron Ramirez
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


def resizear(image, width = None, height = None, inter = cv2.INTER_AREA):
    """
    Cambiar el tamaño de una imagen.
     Parámetros:
        image - Nombre o ruta de la imagen.\n
        [width] - Tamaño ancho. Por defecto ninguno.\n
        [height] - Tamaño alto. Por defecto ninguno.\n
        [inter] - Método de interpolación de openCV. Por INTER_AREA.\n
    Retorna:
        La imagen con tamaño (h,w), (w,w) o (h,h) con el método elegido.
    """
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

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