import cv2 #Cargamos la libreria.

captura=cv2.VideoCapture(0)

while(captura.isOpened()):
    ret,imagen=captura.read()
    cv2.imshow('video',imagen)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
captura.release()
cv2.destroyAllWindows()