#Importando librerias
import cv2#Visión Artificial
import numpy as np #Procesamiento con matrices

#Importando Cascades
clasificador_ojo=cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')
clasificador_rostro=cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_alt.xml')
capturar=cv2.VideoCapture(0) #Iniciar captura de video, donde (n) es el número de cámara escogida

# Definir el codec y crear el objeto VideoWriter
fourCC = cv2.VideoWriter_fourcc('M','S','V','C')#4 caracteres con que se identifica cada códec
out = cv2.VideoWriter('foto.png', fourCC, 25.0, (720, 528))

while(True):#Bucle infinito
        a, frame = capturar.read() #a es un booleano; frame, las imágenes
        imagen=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#cambiar colores a escala de grises y guardar en imagen
        ojos = clasificador_ojo.detectMultiScale(imagen, 1.3, 5)
        rostro = clasificador_rostro.detectMultiScale(imagen, 1.3, 5)
        for (x,y,w,h) in ojos:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),3)
        for (x,y,w,h) in rostro:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(300,255,0),5)
        cv2.imshow('Seguridad Eficiente', frame) #Crear ventana con: (nombre de la ventana, objeto a mostrar)
        if cv2.waitKey(1) & 0xFF == ord('g'):
                out.write(imagen)
                break
        if cv2.waitKey(1) & 0xFF == ord('s'):#Esperar que una tecla se presione y que esta sea la 's'
                break#Saltar bucle
capturar.release()#Liberando recursos
cv2.destroyWindow('Seguridad Eficiente')
#cv2.destroyAllWindows()#Cerrar todas las ventanas creadas