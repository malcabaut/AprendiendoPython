archivo = open("./004 EscribirLeerArchivoTexto/cuentas.txt","r") 
cuentas = [] 
for linea in archivo: 
    linea = linea.replace("\n","") 
    linea = linea.replace(" ","") 
    linea = linea.split("@") 
    for elemento in linea: 
        cuentas.append(elemento) 
archivo.close() 
cuentas_def = [] 
for elemento in cuentas: 
    elemento = elemento.split("=") 
    cuentas_def.append(elemento) 
print(cuentas_def) 
for elemento in cuentas_def: 
    if elemento[0] == "gasto_abril": 
        gasto_abril = elemento[1] 
    elif elemento[0] == "gasto_mayo": 
        gasto_mayo = elemento[1] 
    elif elemento[0] == "gasto_junio": 
        gasto_junio = elemento[1] 
print("El gasto en abril ha sido de",gasto_abril,"euros") 
print("El gasto en mayo ha sido de",gasto_mayo,"euros") 
print("El gasto en junio ha sido de",gasto_junio,"euros") 