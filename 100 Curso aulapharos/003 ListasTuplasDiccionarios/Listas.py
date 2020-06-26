nombres = ["Pedro", "Juan", "Ana"] # Declarmos una lista de nombres.
nombres.append("Maria")# Agregamos un nombre.
print("La variable nombres es del tipo: "+str(type(nombres))
+"  contiene "+str(nombres)
+" y su id en memoria es "
+ str (id(nombres)))
nombres.append("Eva")# Agregamos un nombre, y no se podifica su direcion de memoria
print("La variable nombres es del tipo: "+str(type(nombres))
+"  contiene "+str(nombres)
+" y su id en memoria es "
+ str (id(nombres)))
#Imprimiendo partes de la lista
print("El primer elemento  0: "+nombres[0])
print("El ultimo elemento -1: "+nombres[-1])
nombres.append("Ana")# Agregamos un nombre.
print("La variable nombres es del tipo: "+str(type(nombres))
+"  contiene "+str(nombres)
+" y su id en memoria es "
+ str (id(nombres)))
#Conocer el indice de de la primera Ana
print("El indice de Ana     : "+str(nombres.index("Ana")))
#Modificamos un elemento:
nombres[-1]="Ali"
print("La variable nombres es del tipo: "+str(type(nombres))
+"  contiene "+str(nombres)
+" Tiene "+str(len(nombres))+" elementos"
+" y su id en memoria es "
+ str (id(nombres)))
