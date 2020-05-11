nombres = ['Pedro', 'Juan', 'Ana', 'Maria', 'Eva', 'Ana'] # Declarmos una lista de nombres.
def imp(): # funcion para ver uqe hay en la variable.
    print("La variable nombres es del tipo: "+str(type(nombres))
    +"  contiene "+str(nombres)
    +" Tiene "+str(len(nombres))+" elementos"
    +" y su id en memoria es "
    + str (id(nombres)))
imp()
#inserta en una posision desplazado los demas elemetos a la derecha.
nombres.insert(1,"Leo")
imp()
 # ("Ana" in nombres) devuelve true si esta en la lista
if "Ana" in nombres: print ("Ana está en la lista nombres")