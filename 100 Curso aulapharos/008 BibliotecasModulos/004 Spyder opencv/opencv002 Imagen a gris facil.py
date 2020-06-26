import cv2 #Cargamos la libreria.
miImagen=cv2.imread("Can.jpg", 0) 
cv2.imshow('nombreventana',miImagen)
cv2.waitKey(0) #Espera a que pulse alguna tecla
cv2.destroyAllWindows() #Elimina todas la ventas de windows
