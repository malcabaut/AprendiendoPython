archivo = open("./004 EscribirLeerArchivoTexto/nombres.txt","r") 
nombres = [] 
for linea in archivo: 
   linea = linea.replace("\n","") 
   nombres.append(linea) 
archivo.close() 
print(nombres) 