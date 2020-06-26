nombres = ['Miguel','Ana']
archivo = open("./004 EscribirLeerArchivoTexto/nombres.txt","w")
for nombre in nombres: 
   archivo.write (nombre + "\n") 
archivo.close()