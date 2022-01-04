# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:48:03 2021

@author: Aaron Ramirez
"""
import numpy as np

def ruido_gaussiano(img, prcnt):

    """

    Funcion que genera ruido gaussiano que afecta a un porcentaje de la imagen.

    Parámetros:

        img - Imagen a la que se le aplicará ruido.\n

        prcnt - Porcentaje de pixeles en la imagen al que se agrega el ruido.

    """

    temp = np.float64(np.copy(img))

    tam = img.size

    aux = (tam*prcnt)//100

    cont = 0

    mean = 0

    var = 0.5

    sigma = var ** 0.5

    h = temp.shape[0]

    w = temp.shape[1]

    ruido = np.random.normal(mean, sigma, (1, 1))

    noisy = np.zeros(temp.shape, np.float64)

    for i in range(h):

        for j in range(w):

            temp[i][j] = temp[i][j] + ruido[0][0]

            cont=cont+1

            if(cont>=aux):

                break

        if(cont>=aux):

            break

    noisy = temp

    return noisy