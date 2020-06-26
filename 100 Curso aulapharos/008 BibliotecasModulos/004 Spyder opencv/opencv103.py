import cv2 #Cargamos la libreria.

captura=cv2.VideoCapture(0)

while(captura.isOpened()):
    ultimo,imagen=captura.read()
    cv2.imshow('video',imagen)
    if cv2.waitKey(30) & 0xFF == ord ('q'):
        break
captura.release()
cv2.destroyAllWindows()