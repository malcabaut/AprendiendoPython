#funcion zip para unir 2 listas y crear una diccionario
lista1 = ["Ana", "María", "Juan"]
lista2 = [23, 30, 43]
lista3 = list(zip(lista1,lista2))
print(lista3)
print (str (type(lista3)))
lista3.insert(0,["Eva",22])
print(lista3)
# Se puede crear un diccionario con cualquier cosa iterable
diccionario = dict(zip("abcde","12345"))
print(diccionario)