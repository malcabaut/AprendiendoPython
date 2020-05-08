import re  # para expresiones regulares.
import datetime  # para guardar fechas.
# Solución https://es.stackoverflow.com/questions/353554/introducir-una-fecha-mediante-input
repetir = True  # Variable para controlar el bucle
while repetir == True:  # Comprobamos que la variable se correcta.
    fecha = input("Introduce fecha en formato YYYY,MM,DD ->  ")# Solicitamos fecha
    patron = re.compile(r'^\d{1,},\d{1,},\d{1,}$')# puedes cambiar el patron
    encontrado = patron.search(fecha)
    if encontrado:# si el patron exite intentamos guardarla en datetime.time
        try:# Si la fecha no exite da una excepción 
            fechadate = datetime.date( # guardamos la fecha usando split para dividir el str
                int(fecha.split(",")[0]), 
                int(fecha.split(",")[1]), 
                int(fecha.split(",")[2]))
            repetir = False #todo correcto terminamos el bucle.
        except:
            print("Fecha no valida.")
print(fechadate)
