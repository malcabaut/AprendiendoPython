nombres = ['Pedro', 'Juan', 'Ana', 'Maria', 'Eva', 'Ana','Laura'] # Declarmos una lista de nombres.
def imp(): # funcion para ver uqe hay en la variable.
    print("La variable nombres es del tipo: "+str(type(nombres))
    +"  contiene "+str(nombres)
    +" Tiene "+str(len(nombres))+" elementos"
    +" y su id en memoria es "
    + str (id(nombres)))
imp()
#Elimina un elemetos de una lista por contenido
nombres.remove('Maria')
imp()
#Elimina un elemetos de una lista por opicion
nombres.remove(nombres[1])
imp()
#Elimina la primera
print("Eliminado la primera Ana")
del nombres[nombres.index('Ana')]
imp()
nombres = ['Pedro', 'Juan', 'Ana', 'Maria', 'Eva', 'Ana','Laura'] # Declarmos una lista de nombres.
#Elimina partes
del nombres[2:5]
imp()
nombres = ['Pedro', 'Juan', 'Ana', 'Maria', 'Eva', 'Ana','Laura'] # Declarmos una lista de nombres.
#Elimina desde indice 3 en adelante.
del nombres[3:]
imp()
nombres = ['Pedro', 'Juan', 'Ana', 'Maria', 'Eva', 'Ana','Laura'] # Declarmos una lista de nombres.
#Elimina todos los elementos
del nombres[:]
imp()