#Creamos un diccionario como una libreta de suministros de acero
suministros_acero = {"Aceralia":["636777888","info@aceralia.com"],
"Aceros Mateo":["679888123","acerosmateo@gmail.com"]}
print("Aceralia: "+str (suministros_acero["Aceralia"])) # imprimimos los datos de Aceralia
suministros_acero["Hierros Mategui"] = ["699887678", "infomategui@hotmail.com"]
# Imprimimos la lista entera:
print(suministros_acero)
del suministros_acero['Aceralia'] # Eliminamos un elemento del diccionario
print(suministros_acero)

for i in suministros_acero:
 print ("Nombre: "+i+" | Datos: "+str(suministros_acero[i]))