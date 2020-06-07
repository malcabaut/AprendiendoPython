import cv2 #Cargamos la libreria.
import numpy as np
#Cargamos la imagen en una variable. es un array numpy
miImagen=cv2.imread("CandelariaAlfarnate2019.JPG", cv2.IMREAD_COLOR) 
print("El tipo de la variable miImagen es: ",type(miImagen)) 
print("Las dimensiones de miImagen son: ",miImagen.shape)
 
scale_percent = 20 #Porcentaje de la escala
width = int(miImagen.shape[1] * scale_percent / 100) #Cambio ancho
height = int(miImagen.shape[0] * scale_percent / 100) #Cambio alto
dim = (width, height) #Tamaño de la imagen de salida

interpolation = cv2.INTER_AREA
# Redimesion de la imagen
resized = cv2.resize(miImagen, dim, interpolation)

red=np.zeros(resized.shape, dtype=miImagen.dtype)
red[:,:,2]=resized[:,:,2] 
cv2.imshow("Rojo", red) #Mostamos la imagen redimesionada

green=np.zeros(resized.shape, dtype=miImagen.dtype)
green[:,:,1]=resized[:,:,1] 
cv2.imshow("Verde", green) #Mostamos la imagen redimesionada

blue=np.zeros(resized.shape, dtype=miImagen.dtype)
blue[:,:,0]=resized[:,:,0] 
cv2.imshow("Blue", blue) #Mostamos la imagen redimesionada

cv2.waitKey(0) #Espera a que pulse alguna tecla
cv2.destroyAllWindows() #Elimina todas la ventas de windows