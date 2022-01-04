import cv2
from skimage.util import noise
import imutils1 as im
import numpy as np
import matplotlib.cm as cm
import skimage.util as ut
from matplotlib import pyplot as plt
from skimage.morphology import disk
from skimage.filters.rank import median
from skimage.util import view_as_blocks
#https://pythoneyes.wordpress.com/2017/06/23/anadir-ruido-a-imagenes-con-python/
#https://programmerclick.com/article/61052292706/

#img = im.resizear(cv2.imread('Fotos/Fig0312(a)(kidney).tif',0),400)
img = im.resizear(cv2.imread('Fig0312(a)(kidney).tif',cv2.IMREAD_GRAYSCALE), 400)
numero = (img.size * 60 ) / 100

ruido = im.gasuss_noise(img,mean=0.8)
#noisy_image=ut.add_gaussian_noise(img,3)
#noisy_image=ut.add_gaussian_noise(img,6)

#gauss = np.random.normal(0, 0.5, (img.shape[0],img.shape[1]))

#ruido = im.ruido_gaussiano(img, 100)
#gauss = np.random.normal(0, 0.5, (img.shape[0],img.shape[1]))
tmp = np.float64(np.copy(img))
#ruido = np.zeros(tmp.shape, np.float64)
#img2 = np.array(img.shape)
# ruido = tmp + ruido
ruido = ruido.astype(np.uint8)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
histR = cv2.calcHist([ruido], [0], None, [256], [0, 256])
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Imagen Original')
plt.axis('off')
plt.subplot(122), plt.imshow(ruido, 'gray'), plt.title('Imagen Con Ruido')
plt.axis('off')
#plt.subplot(223), plt.plot(histT), plt.xlabel('Intensidad de Iluminacion'), plt.ylabel('Cantidad de Pixeles')
#plt.subplot(224), plt.plot(histR), plt.xlabel('Intensidad de Iluminacion'), plt.ylabel('Cantidad de Pixeles')
# #Plot
# plt.subplot(223)
# plt.plot(hist, color='r', label='Original')
# plt.plot(histR, color='b', label='Ruido')
# plt.xlabel('Intensidad de Iluminacion'), plt.ylabel('Cantidad de Pixeles')
# plt.legend()
plt.show()


mean = 0
var = 0.1
sigma = var**0.5
gaus = np.random.normal(mean,0.5,(img.shape[0],img.shape[1]))
temp_image = np.float64(np.copy(img))
noisy_image = np.zeros(temp_image.shape, np.float64)
noisy_image = temp_image + gaus
kernel_1= (1/9)*(np.ones((3,3), dtype= np.float32))
gaus_1= cv2.filter2D(noisy_image,-1,kernel_1)
plt.subplot(131), plt.imshow(img, "gray"), plt.title("Img. Original"), plt.axis("off")
plt.subplot(132), plt.imshow(noisy_image, "gray"), plt.title("Img. con ruido"), plt.axis("off")
plt.subplot(133), plt.imshow(gaus_1, "gray"), plt.title("Ventana de 3x3"), plt.axis("off")
plt.show()




gaus = np.random.normal(mean,2,(img.shape[0],img.shape[1]))
temp_image = np.float64(np.copy(img))
noisy_image = np.zeros(temp_image.shape, np.float64)
noisy_image = temp_image + gaus
kernel_1= (1/16)*(np.ones((4,4), dtype= np.float32))
gaus_1= cv2.filter2D(noisy_image,-1,kernel_1)
plt.subplot(131), plt.imshow(img, "gray"), plt.title("Imagen Original"), plt.axis("off")
plt.subplot(132), plt.imshow(noisy_image, "gray"), plt.title("Img. Con ruido"), plt.axis("off")
plt.subplot(133), plt.imshow(gaus_1, "gray"), plt.title("Ventana de 4x4"), plt.axis("off")
plt.show()


gaus = np.random.normal(mean,4,(img.shape[0],img.shape[1]))
temp_image = np.float64(np.copy(img))
noisy_image = np.zeros(temp_image.shape, np.float64)
noisy_image = temp_image + gaus
kernel_1= (1/20)*(np.ones((5,5), dtype= np.float32))
#Filtra la imagen utilizando la Ventan
gaus_1= cv2.filter2D(noisy_image,-1,kernel_1)
plt.subplot(131), plt.imshow(img, "gray"), plt.title("Imagen Original"), plt.axis("off")
plt.subplot(132), plt.imshow(noisy_image, "gray"), plt.title("Img. Con ruido"), plt.axis("off")
plt.subplot(133), plt.imshow(gaus_1, "gray"), plt.title("Ventana de  5x5"), plt.axis("off")
plt.show()