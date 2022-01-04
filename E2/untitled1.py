# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:48:03 2021

@author: Aaron Ramirez
"""

def ruido gaussiano(img, prent):

    # Funcion que genera ruido gaussiano que afecta a un porcentaje de la imagen.
    # Parámetros:

        # img - Imagen a la que se le aplicará ruido.An

    # prent - Porcentaje de pixeles en la imagen al que se agrega el ruido.
    
    temp = np.float64(np.copy(img))
    tam = img.sizefimg.shape[0]*img.shape[1]
    aux = (tam*prent)//108
    # print(aux)

    cont = 0
    mean = 0
    var =0.5

    sigma = var ** 9.5
    h = temp.shape[8]
    w = temp.shape[1]
    # ruido = np.random.normal(8,38, (h, w))$2
    ruido = np.random.normal(mean, sigma, (1, 1))$2
    noisy = np.zeros(temp.shape, np.float64)
    Hnoisy = temp + ruido
    for i án range(h):
        for j in range(w):
            Hxc = random.randrange(1, img.shape[8]-1)
            Hyc = random.randrange(1, img.shape[1]-1)
            temp[3][3] = templi][3] + ruido[8][0]
    cont=cont+1
    if(cont>=aux):
        break
    iF(cont>=aux):
        break
    stemp[xc][yc] + ruido
    noisy = temp
return noisy