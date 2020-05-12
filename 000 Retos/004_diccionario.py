# Reto propuesto por el curso que estoy siguiendo de Structuralia (https://sando.aulapharos.com/).
# Tema4 Listas, tuplas y diccionarios (condicionales y bucles)
'''
Crea un script que te dé los materiales necesarios para elaborar varios tipos de
cementos, morteros y hormigones, a petición del usuario. 
El script debe indicar qué opciones pueden ser elegidas por el usuario 
y, posteriormente, al elegir una, indicar los materiales necesarios. Usa un diccionario para almacenar las traducciones.
'''
import time
materiales = {"cementos1": ["componente2", "componente2"],
                "cementos2": ["componente3", "componente15"],
                "cementos3": ["componente4", "componente75"],
                "morteros1": ["componente5", "componente35"],
                "morteros2": ["componente6", "componente11"],
                "hormigones1": ["componente2", "componente2"],
                "hormigones2": ["componente1", "componente3"],
                "hormigones3": ["componente3", "componente44"], }

print(str (materiales))
repetir = True  # Variable para controlar el bucle
while repetir == True:  # Comprobamos que la variable se correcta.
    print ("Tipo de materiales : ")
    for i in materiales:
    #print ("¿Que tipo de material quieres?: "+i+" | Datos: "+str(materiales[i]))
        print ("   "+i)
    seleccion = input("¿Que tipo de material quieres?: ")
    if seleccion in materiales: 
        repetir=False  
        print ("Este material esta compuesto por: "+str (materiales[seleccion]))
    else:
        print ("------------El material no esta diponible.----------")
        time.sleep(1)