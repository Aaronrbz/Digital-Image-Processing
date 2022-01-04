# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:29:57 2021

@author: Aaron Ramirez
"""

import numpy as np
import cv2
import detectarbordes as borde
import matplotlib.pyplot as plt



from math import sqrt

######### Robert ##################
mRobersX= np.array([[0,0,0],[0,0,1],[0,-1,0]])
mRobersY= np.array([[-1,0,0],[0,1,0],[0,0,0]])


######## Sobel ###################
mSobelX= (1/4)*(np.array([[1,0,-1],[2,0,-2],[1,0,-1]],dtype=float))
mSobelY= (1/4)*(np.array([[-1,-2,-1],[0,1,0],[1,2,1]],dtype=float))


######## Prewitt #################
mPrewittX = (1/3)*(np.array([[1,0,-1],[1,0,-1],[1,0,-1]],dtype=float))
mPrewittY = (1/3)*(np.array([[-1,-1,-1],[0,1,0],[1,1,1]],dtype=float))

######## Frei-che ################
aux = (1/(2+sqrt(2)))
r=sqrt(2)
mfreiX= aux* (np.array([[1,0,-1],[r,0,-r],[1,0,-1]],dtype=float))
mfreiY= aux* (np.array([[-1,-r,-1],[0,1,0],[1,r,1]],dtype=float))

###### Lerr imagen #####
ruta1 = "105_7.tif"
image = cv2.imread(ruta1,0)
image1 = cv2.imread(ruta1)


imagen = cv2.imread("105_7.tif", 0)
image1 = cv2.cvtColor(cv2.imread("105_7.tif", 0), cv2.COLOR_BGR2RGB)

salidax = cv2.filter2D(image, -1, mRobersX)
saliday = cv2.filter2D(image, -1, mRobersY)

imgris = salidax+saliday
cv2.imwrite('mejorado.png',imgris)
plt.imshow(imgris,cmap="gray")

# borde.detect_border(ruta1,mSobelX, mSobelY, "Sobel")
# borde.detect_border(ruta1, mPrewittX,mPrewittY, "Prewitt")
# borde.detect_border(ruta1,mfreiX, mfreiY, "Frei-Che")

# ######### Añadir ruido S&P ###########
# imagensp=borde.sp_noise(image1, 0.08)
# cv2.imwrite("fachada-de-casa-sp.jpg",imagensp)
# imagensp1="fachada-de-casa-sp.jpg"

# ########## Mostrar con ruido #######

# borde.detect_border(imagensp1, mRobersX, mRobersY, "Robers Con ruido")
# borde.detect_border(imagensp1,mSobelX, mSobelY, "Sobel Con ruido")
# borde.detect_border(imagensp1, mPrewittX,mPrewittY, "Prewitt Con ruido")
# borde.detect_border(imagensp1,mfreiX, mfreiY, "Frei-Che Con ruido")
