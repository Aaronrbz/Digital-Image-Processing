import numpy as np
import cv2
from matplotlib import pyplot as plt
import imutils as im 


def ruido_gaussiano(img, prcnt):
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


id = 'Fig0312(a)(kidney).tif'

image = cv2.imread(id,0)

noisy_image=ruido_gaussiano(image,5)


plt.subplot(221), plt.imshow(image, "gray"), plt.title("Original"), plt.axis("off")
plt.subplot(222), plt.imshow(noisy_image, "gray"), plt.title("Con ruido"), plt.axis("off")
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
noisy_image = noisy_image.astype(np.uint8)
hist_R = cv2.calcHist([noisy_image], [0], None, [256], [0, 256])

plt.subplot(223)
plt.plot(hist, color="r", label = "Original")
plt.plot(hist_R, color="b", label = "Ruido"),plt.xlabel('intensidad de iluminacion'),plt.ylabel('cantidad de pixeles')
plt.legend(loc='upper right')
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------
mean = 0
var = 0.1
sigma = var**0.5
gaus = np.random.normal(mean,sigma,(image.shape[0],image.shape[1]))
temp_image = np.float64(np.copy(image))
noisy_image = np.zeros(temp_image.shape, np.float64)
noisy_image = temp_image + gaus
#noisy_image = noisy_image.astype(np.uint8)

plt.subplot(121), plt.imshow(image, "gray"), plt.title("Original"), plt.axis("off")
plt.subplot(122), plt.imshow(noisy_image, "gray"), plt.title("Con ruido"), plt.axis("off")
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------

mean = 0
var = 1
sigma = var**1
gaus = np.random.normal(mean,0.5,(image.shape[0],image.shape[1]))
temp_image = np.float64(np.copy(image))
noisy_image = np.zeros(temp_image.shape, np.float64)
noisy_image = temp_image + gaus
kernel_1= (1/9)*(np.ones((3,3), dtype= np.float32))
 
#Filtra la imagen utilizando el kernel anterior
gaus_1= cv2.filter2D(noisy_image,-1,kernel_1)

plt.subplot(131), plt.imshow(image, "gray"), plt.title("Original"), plt.axis("off")
plt.subplot(132), plt.imshow(noisy_image, "gray"), plt.title("Con ruido"), plt.axis("off")
plt.subplot(133), plt.imshow(gaus_1, "gray"), plt.title("Filtrado 3*3"), plt.axis("off")
plt.show()

#################################################################################################
gaus = np.random.normal(mean,2,(image.shape[0],image.shape[1]))
temp_image = np.float64(np.copy(image))
noisy_image = np.zeros(temp_image.shape, np.float64)
noisy_image = temp_image + gaus
kernel_1= (1/16)*(np.ones((4,4), dtype= np.float32))

#Filtra la imagen utilizando el kernel anterior
gaus_1= cv2.filter2D(noisy_image,-1,kernel_1)

plt.subplot(131), plt.imshow(image, "gray"), plt.title("Original"), plt.axis("off")
plt.subplot(132), plt.imshow(noisy_image, "gray"), plt.title("Con ruido"), plt.axis("off")
plt.subplot(133), plt.imshow(gaus_1, "gray"), plt.title("Filtrado 4*4"), plt.axis("off")
plt.show()

##################################################################################################
gaus = np.random.normal(mean,4,(image.shape[0],image.shape[1]))
temp_image = np.float64(np.copy(image))
noisy_image = np.zeros(temp_image.shape, np.float64)
noisy_image = temp_image + gaus
kernel_1= (1/20)*(np.ones((5,5), dtype= np.float32))
 
#Filtra la imagen utilizando el kernel anterior
gaus_1= cv2.filter2D(noisy_image,-1,kernel_1)

plt.subplot(131), plt.imshow(image, "gray"), plt.title("Original"), plt.axis("off")
plt.subplot(132), plt.imshow(noisy_image, "gray"), plt.title("Con ruido"), plt.axis("off")
plt.subplot(133), plt.imshow(gaus_1, "gray"), plt.title("Filtrado 5*5"), plt.axis("off")
plt.show()