import cv2
from skimage.util import noise
import imutils1 as im
import numpy as np
import matplotlib.cm as cm
import skimage.util as ut
from matplotlib import pyplot as plt
from skimage.morphology import disk
from skimage.filters.rank import median
#https://pythoneyes.wordpress.com/2017/06/23/anadir-ruido-a-imagenes-con-python/
#https://programmerclick.com/article/61052292706/

img = im.resizear(cv2.imread('Fig0312(a)(kidney).tif',cv2.IMREAD_GRAYSCALE), 400)
numero = (img.size * 60 ) / 100
#print(numero)
#cv2.imshow('ORIGINAL',img)

# hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# plt.plot(hist, color='gray')
# plt.xlabel('Intensidad de Iluminación')
# plt.ylabel('Cantidad de Pixeles')
# plt.show()

# ruido = im.ruido_gaussiano(img, 50)
#gauss = np.random.normal(0, 4, (img.shape[0],img.shape[1]))

gauss1 = np.random.normal(0.2, 0.5, (img.shape[0],img.shape[1]))
gauss2 = np.random.normal(0.2, 2, (img.shape[0],img.shape[1]))
gauss3 = np.random.normal(0.2, 4, (img.shape[0],img.shape[1]))

# gauss1 = np.random.normal(0.3, 0.5, (img.shape[0],img.shape[1]))
# gauss2 = np.random.normal(0.3, 2, (img.shape[0],img.shape[1]))
# gauss3 = np.random.normal(0.3, 4, (img.shape[0],img.shape[1]))

#gauss1 = np.random.normal(0.6, 0.5, (img.shape[0],img.shape[1]))
#gauss2 = np.random.normal(0.6, 2, (img.shape[0],img.shape[1]))
#gauss3 = np.random.normal(0.6, 4, (img.shape[0],img.shape[1]))

tmp = np.float64(np.copy(img))
ruido3 = ruido2 = ruido1 = np.zeros(tmp.shape, np.float64)
#img2 = np.array(img.shape)
ruido1 = tmp + gauss1
ruido2 = tmp + gauss2
ruido3 = tmp + gauss3
ruido1 = ruido1.astype(np.uint8)
ruido2 = ruido2.astype(np.uint8)
ruido3 = ruido3.astype(np.uint8)

#hist = cv2.calcHist([img], [0], None, [256], [0, 256])
#histR = cv2.calcHist([ruido3], [0], None, [256], [0, 256])
plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Imagen Original')
plt.axis('off')
plt.subplot(222), plt.imshow(ruido1, 'gray'), plt.title('Imagen Con σ=0.5')
plt.axis('off')
plt.subplot(223), plt.imshow(ruido2, 'gray'), plt.title('Imagen Con σ=2')
plt.axis('off')
plt.subplot(224), plt.imshow(ruido3, 'gray'), plt.title('Imagen Con σ=4')
plt.axis('off')

# plt.subplot(223), plt.plot(hist), plt.xlabel('Intensidad de Iluminacion'), plt.ylabel('Cantidad de Pixeles')
# plt.subplot(224), plt.plot(histR), plt.xlabel('Intensidad de Iluminacion'), plt.ylabel('Cantidad de Pixeles')

plt.show()
#VENTANAS
w_05 = (1/9)*(np.ones((3,3), dtype=np.float32))
w_02 = (1/9)*(np.ones((4,4), dtype=np.float32))
w_04 = (1/9)*(np.ones((5,5), dtype=np.float32))

filtrado1 = median(ruido1, w_05)
filtrado2 = median(ruido2, w_02)
filtrado3 = median(ruido3, w_04)

#histo = cv2.calcHist([img], [0], None, [256], [0, 256])
#histF = cv2.calcHist([filtrado], [0], None, [256], [0, 256])
plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Imagen Original')
plt.axis('off')
plt.subplot(222), plt.imshow(filtrado1, 'gray'), plt.title('Ventana 3x3')
plt.axis('off')
plt.subplot(223), plt.imshow(filtrado2, 'gray'), plt.title('Ventana 4x4')
plt.axis('off')
plt.subplot(224), plt.imshow(filtrado3, 'gray'), plt.title('Ventana 5x5')
plt.axis('off')
# plt.subplot(223), plt.plot(histo), plt.xlabel('Intensidad de Iluminacion'), plt.ylabel('Cantidad de Pixeles')
# plt.subplot(224), plt.plot(histF), plt.xlabel('Intensidad de Iluminacion'), plt.ylabel('Cantidad de Pixeles')
plt.show()


#cv2.normalize(noisy, noisy, 0, 255, cv2.NORM_MINMAX, dtype=-1)
#noisy = noisy.astype(np.uint8)
# cv2.imshow('Con Ruido', noisy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()