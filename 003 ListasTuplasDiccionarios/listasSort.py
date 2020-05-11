nombres = ['Pedro', 'Juan', 'Ana', 'Maria', 'Eva', 'Ana'] # Declarmos una lista de nombres.
def imp(): # funcion para ver uqe hay en la variable.
    print("La variable nombres es del tipo: "+str(type(nombres))
    +"  contiene "+str(nombres)
    +" Tiene "+str(len(nombres))+" elementos"
    +" y su id en memoria es "
    + str (id(nombres)))
imp()
#Ordenamos una lista
nombres.sort()
imp()
#Ordenamos una lista al reves
nombres.sort( reverse=True)
imp()
