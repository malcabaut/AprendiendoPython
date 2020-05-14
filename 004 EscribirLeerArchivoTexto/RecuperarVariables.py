archivo = open("./004 EscribirLeerArchivoTexto/nombres.txt","r")
lista=[]
for linea in archivo:
    print(linea)
    lista.append(linea)
archivo.close()
print(lista)