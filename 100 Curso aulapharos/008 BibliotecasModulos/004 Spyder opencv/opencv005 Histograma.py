import cv2 #Cargamos la libreria.
import numpy as np
from matplotlib import pyplot as plt
#Cargamos la imagen en una variable. es un array numpy
miImagen=cv2.imread("CandelariaAlfarnate2019.JPG", cv2.IMREAD_COLOR) 
print("El tipo de la variable miImagen es: ",type(miImagen)) 
print("Las dimensiones de miImagen son: ",miImagen.shape)
 
scale_percent = 20 #Porcentaje de la escala
width = int(miImagen.shape[1] * scale_percent / 100) #Cambio ancho
height = int(miImagen.shape[0] * scale_percent / 100) #Cambio alto
dim = (width, height) #Tamaño de la imagen de salida

interpolation = cv2.COLOR_BGR2GRAY
# Redimesion de la imagen
resized = cv2.resize(miImagen, dim, interpolation)

hist = cv2.calcHist([resized],[0],None,[256],[0,256]) 
plt.plot(hist) 
plt.xlim([0,256]) 
plt.title("Histograma imagen 1 en blanco y negro")
plt.show() 
 