import cv2


camera=cv2.VideoCapture(1)#Digitamos el argumento de entrada para una camara o un archivo de video
# 0 si solo tenes una camara conectada, o 1 si tenes otra secundaria.

if(camera.isOpened()):
    print("The camera is successfully opened")
else:
    print("Error: The camera is not opened")

while True:
    success, frame =camera.read()#Leemos la camara
    if not success:
        print("Error: Couldn't read the camera")
        break
    cv2.imshow("Camera",frame)#Mostramos la imagen

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break #Si presionamos la tecla q se cierra la ventana

camera.release()#Liberamos la camara
cv2.destroyAllWindows()#Cerramos todas las ventanas