# Reto propuesto por el curso que estoy siguiendo de Structuralia (https://sando.aulapharos.com/).
# Tema3 Elementos de control (condicionales y bucles)
'''
Realiza un programa que realice una cuenta atrás de una cantidad de tiempo (minutos y segundos) introducida por el usuario.
Dicho programa deberá contar cuántos minutos quedan a no ser que quede menos de un minuto, que contará segundos a segundos.
Así mismo, deberá obligar al usuario a introducir un número como input.
'''
# Voy a aprovecha para intentar hacer validacion de entrada CON EXPRESIONES REGULARES (En java lo realizo con Pattern Matcher)

import time
import re  # hay que importa la libreria re

repetir = True #Variable para controlar el bucle
while repetir == True: #Comprobamos que la variable se correcta.
    entrada=input("Introduce una minutos y segundos (ejemplo 55:11) ->  ")
    patron = re.compile(r'^\d{1,}:\d{1,}$') 
    encontrado = patron.search(entrada) 
    if encontrado: repetir = False

minutos=int(entrada.split(":")[0])
segundos=int(entrada.split(":")[1])

minutos = minutos + segundos//60
segundos = segundos%60
print("Has introducido: "+ str(minutos) +" minutos.")
print("Has introducido: "+ str(segundos) +" segundos.")
print("Lo que son unos "+ str(segundos+minutos*60) +" segundos.")
segundos=segundos+minutos*60

# Contado segundos
while segundos >= 0:
    print( "Quedan "+str(segundos//60)+" minutos. Cuenta atras :"+str(segundos)+" segundos.")
    segundos = segundos - 1
    time.sleep(1)