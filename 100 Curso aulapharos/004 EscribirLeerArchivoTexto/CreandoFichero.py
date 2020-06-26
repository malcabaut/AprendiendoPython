nombres = ['Miguel','Ana','Laura']
archivo = open("nombres.txt","w") # Con w sobre escribimos
for nombre in nombres:
 archivo.write(nombre + "\n")
archivo.close()

nombres = ['Eva','Toni','Mk'] 
archivo = open("nombres.txt","a") # Con a añadimos
for nombre in nombres:
 archivo.write(nombre + "\n")
archivo.close()

nombres = ['Sara','Daniel','Noa']
archivo = open("nombres.txt","w") # Con w sobre escribimos
for nombre in nombres:
 archivo.write(nombre + "\n")
archivo.close()

archivo = open("nombres.txt","r") # Leemos el fichero con r
contenido = archivo.read()
print (contenido)
archivo.close()
