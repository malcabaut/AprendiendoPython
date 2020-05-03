# No es neceario declarar el tipo de variables antes de asignarla.
####
#   Tipos cadenas
####
nombre = 'Tiffany'
# Strings se crean con " o '
apellido = "Dolorido"
# Los strings se puede concadenar
print(nombre+" "+apellido)
# Se puede conocer el tipo de la variable con type(variable)
print(type(nombre))  # el tipo string es (str)

# Un string puede ser tratado como una lista de caracteres
print(nombre[0])
# % pueden ser usados para formatear strings
"%s pueden ser %s" % ("strings", "interpolados")
print("Nombre: %s\n Apellido: %s "%(nombre.upper()[0:5].replace('F','f'),apellido.lower()))

####
#   Tipos numericos
####
entero = 45  # Tipos enteros (int)
# Puedes realizar traformaciones entre tipos distintos
print("El numero " + str(entero)+" es del tipo " + str(type(entero)))
flotante = 50.23  # Tipo flotantes (float)
print("El numero " + str(flotante)+" es del tipo " + str(type(flotante)))
complejo = 4 + 50.23j  # Tipo complejos (complex)
print("El numero " + str(complejo)+" es del tipo " + str(type(complejo)))

####
#   Tipos booleanos
####
continuarFlujo = True
continuarFlujo = False

print("Continuar Flujo es: "+str(continuarFlujo) +
      " Que es de la clase: " + str(type(continuarFlujo)))

####
#   Tipos lista
####
lista = ['texto', 45, 13.14, 4 + 2j, True]
print("Esto es un Array de varios tipos "+str(lista) +
      " tipo en python: " + str(type(lista)))
lista[0] = "Cambio"
print("Esto es un Array de varios tipos "+str(lista) +
      " tipo en python: " + str(type(lista)))
####
#   Tipos tupla
####
lista = ('texto', 45, 13.14, 4 + 2j, True)
print("Esto es un tupla de varios tipos "+str(lista) +
      " tipo en python: " + str(type(lista)))

""" Esto no funcionaria ya que las tuplas no puede ser cambiadas.     
lista[0] = "Cambio"
print("Esto es un tupla de varios tipos "+str(lista) +
      " tipo en python: " + str(type(lista)))
"""
####
#   Tipos diccionarios
####
diccionario = {"rojo":"FF0000","verde":"00FF00","azul":"0000FF"}
print("Esto es un diccionario de colores "+str(diccionario) +
      " tipo en python: " + str(type(diccionario)))

####
#   Tipos vacio
####
celebro = None
print("Que hay en esta variable llamada celebro: "+str(celebro) +
      " tipo en python: " + str(type(celebro)))