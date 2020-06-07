import cv2 #Cargamos la libreria.
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

interpolation = cv2.COLOR_BGR2GRAY
# Imagen en gris
grey = cv2.cvtColor(resized, interpolation)
 
print("Las dimensiones de miImagen redimensionada son: ",miImagen.shape)

 
cv2.imshow('image',grey) #Mostramos la imagen gris
cv2.imshow("Resized image", resized) #Mostamos la imagen redimesionada
cv2.waitKey(0) #Espera a que pulse alguna tecla
cv2.destroyAllWindows() #Elimina todas la ventas de windows
