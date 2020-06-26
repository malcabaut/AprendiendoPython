gasto_abril = 18234 
gasto_mayo = 209123 
gasto_junio = 87690 
 
archivo = open("./004 EscribirLeerArchivoTexto/cuentas.txt","a") 
archivo.write("gasto_abril = "+str(gasto_abril)) 
archivo.write("@gasto_mayo = "+str(gasto_mayo)) 
archivo.write("@gasto_junio = "+str(gasto_junio)) 
archivo.close()