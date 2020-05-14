'''
Trata de crear un script que guarde una lista de nombres en un archivo ya existente que
contenga una lista, leyendo previamente la lista. Inicialmente tendremos que abrir el archivo
con cuidado de que, en caso de no existir, Python nos dará un error (prueba con un try -
except).
El script nos tendrá que dar la opción de utilizar los nombres existentes en la lista y seguir
incorporando nuevos o bien eliminarlos todos y empezar de cero.
'''
'''
Podria hacerlo con un if
import os
print("El fichero existe.") if os.path.exists(
    "fichero.txt") else print("Fichero no existe.")
'''
repetir = True  # Variable para controlar el bucle
list = []

try:  # Intentamos abrir el fichero.
    # Abrimos el fichero para extraer la lista de nombres.
    archivo = open("./000 Retos/fichero.txt", "r")
    for linea in archivo:
        linea = linea.replace("\n","")
        list.append(linea)
    archivo.close()
except:  # Si no es posible creamos un nuevo fichero.
    archivo = open("./000 Retos/fichero.txt", "w")  # Creamos el fichero
    archivo.close()


def Salir():
    global repetir, list
    print("Salir")
    archivo = open("./000 Retos/fichero.txt", "a")  # Creamos el fichero
    for linea in list:
        archivo.write(linea +"\n")
    archivo.close()
    repetir = False


def Agregar():
    print("Agregar")
    list.append(input("Introduce nombre: "))


def Imprimir():
    print("Imprimir")
    print(list)


def Eliminar():
    print("Eliminar")


# Creamos un diccionario con las elecciones posibles.
elecciones = {0: Salir, 1: Agregar, 2: Eliminar, 3: Imprimir}
while repetir == True:  # Comprobamos que la variable se correcta.
    print('''
    #####  Gestion Agenda   #####
    #   0.- Salir.              #
    #   1.- Agregar.            #
    #   2.- Eliminar.           #
    #   3.- Imprimir.           #
    #############################
    ''')
    try:
        seleccion = int(input('Escoge una opcion: '))
    except:
        print("Utilicen los numeros")
    elecciones[seleccion]() if (0 <= seleccion & 3 >= seleccion) else print(
        "Selecciona una de las opciones")

