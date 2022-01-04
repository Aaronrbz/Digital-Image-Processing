import imutils as im
import cv2
from skimage.util import random_noise
from skimage import filters
from skimage.morphology import disk
import matplotlib.pyplot as plt
import matplotlib.cm as cm

ruta1 = 'test_gray.jpg'
imagen = cv2.imread(ruta1,cv2.IMREAD_GRAYSCALE)
#Tipos de ruido
imgSalt = random_noise(imagen, mode='salt')
imgPepper = random_noise(imagen, mode='pepper')
imgGaussian1 = random_noise(imagen, mode='gaussian', var = 0.2)
imgGaussian2 = random_noise(imagen, mode='gaussian', var = 1.2)
imgLocalvar = random_noise(imagen, mode='localvar')
imgSp = random_noise(imagen, mode='s&p')

#Mediana
fib, axes = plt.subplots(3, 4)
ax = axes.ravel()
#Salt
ax[0].set_title("Sal")
ax[0].imshow(imgSalt, cmap = cm.Greys_r) 
ax[1].set_title("Sal\nMediana")
ax[1].imshow(filters.rank.median(imgSalt,disk(3)), cmap = cm.Greys_r) 
#Pepper
ax[2].set_title("Pimienta")
ax[2].imshow(imgPepper, cmap = cm.Greys_r) 
ax[3].set_title("Pimienta\nMediana")
ax[3].imshow(filters.median(imgPepper,disk(3)), cmap = cm.Greys_r) 
#Localvar
ax[4].set_title("Localvar")
ax[4].imshow(imgLocalvar, cmap = cm.Greys_r) 
ax[5].set_title("Localvar\nMediana")
ax[5].imshow(filters.median(imgLocalvar,disk(3)), cmap = cm.Greys_r) 
#s&p
ax[6].set_title("Sal y Pimienta")
ax[6].imshow(imgSp, cmap = cm.Greys_r) 
ax[7].set_title("S & P\nMediana")
ax[7].imshow(filters.median(imgSp,disk(3)), cmap = cm.Greys_r) 
#Gaussian < 1
ax[8].set_title("Gaussian <1")
ax[8].imshow(imgGaussian1, cmap = cm.Greys_r) 
ax[9].set_title("Gaussian <1\nMediana")
ax[9].imshow(filters.median(imgGaussian1,disk(3)), cmap = cm.Greys_r) 
#Gaussian > 1
ax[10].set_title("Gaussian >1")
ax[10].imshow(imgGaussian2, cmap = cm.Greys_r) 
ax[11].set_title("Gaussian >1\nMediana")
ax[11].imshow(filters.median(imgGaussian2,disk(3)), cmap = cm.Greys_r) 
for a in ax:
    a.axis("off")
plt.tight_layout()
plt.show()

#Promedio 3x3
fib, axes = plt.subplots(3, 4, sharex = True, sharey = True)
ax = axes.ravel()
#Salt
ax[0].set_title("Salt")
ax[0].imshow(imgSalt, cmap = cm.Greys_r) 
ax[1].set_title("Salt\nPromedio")
ax[1].imshow(filters.rank.mean(imgSalt,disk(4)), cmap = cm.Greys_r) 
#Pepper
ax[2].set_title("Pepper")
ax[2].imshow(imgPepper, cmap = cm.Greys_r) 
ax[3].set_title("Pepper\nPromedio")
ax[3].imshow(filters.rank.mean(imgPepper,disk(4)), cmap = cm.Greys_r) 
#Localvar
ax[4].set_title("Localvar")
ax[4].imshow(imgLocalvar, cmap = cm.Greys_r) 
ax[5].set_title("localvar\nPromedio")
ax[5].imshow(filters.rank.mean(imgLocalvar,disk(4)), cmap = cm.Greys_r) 
#s&p
ax[6].set_title("S&P")
ax[6].imshow(imgSp, cmap = cm.Greys_r) 
ax[7].set_title("S&P\nPromedio")
ax[7].imshow(filters.rank.mean(imgSp,disk(4)), cmap = cm.Greys_r) 
#Gaussian < 1
ax[8].set_title("Gausiano <1")
ax[8].imshow(imgGaussian1, cmap = cm.Greys_r) 
ax[9].set_title("Gaussiano <1\nPromedio")
ax[9].imshow(filters.rank.mean(imgGaussian1,disk(4)), cmap = cm.Greys_r) 
#Gaussian > 1
ax[10].set_title("Gaussiaon >1")
ax[10].imshow(imgGaussian2, cmap = cm.Greys_r) 
ax[11].set_title("Gaussiano >1\nPromedio")
ax[11].imshow(filters.rank.mean(imgGaussian2,disk(4)), cmap = cm.Greys_r) 
for a in ax:
    a.axis("off")
plt.tight_layout()
plt.show()


