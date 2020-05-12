# Reto propuesto por el curso que estoy siguiendo de Structuralia (https://sando.aulapharos.com/).
# Tema4 Listas, tuplas y diccionarios (condicionales y bucles)
'''
Crea un script que busque, hasta el número que el usuario indique, los números primos y los
vaya guardando en una lista y posteriormente imprima la lista. Para ello te doy las siguientes
pistas:
 Un número primo sólo se puede dividir entre 1 y sí mismo, por lo que cualquier otra
división dará decimales o, dicho de otra forma, tendrá resto.
 Para saber si un número es primo basta con dividirlo entre todos los números primos
menores que ese número, si el resultado de esas divisiones tiene resto (es decir, % !=
0) ese número es primo.
'''

# Variable para controlar el bucle y repetir mientras los datos introducido no sean numeros.
repetir = True
while repetir == True:  # Comprobamos que la variable se correcta.
    try:  # intentamos guardar en numero1 y numero2 float si no es posible la conversion da un fallo.
        numeroMax = int(input("¿Hasta que número buscar los primos? : "))
        repetir = False  # si llega aqui todo va bien y el codigo continua.
    except:  # en caso de que falle indicamos que tiene que introducir 2 numeros.
        print("Tiene que introducir un numero entero.")


#numeroMax = 100
primos = []
for numero in range(1, numeroMax+1):
    # Tiene que empezar el el 2 ya que todos los numeros son divisibles por 1
    for divisor in range(2, numero):
        if numero % divisor != 0:
          continue
        else:
            break  # Salimos del bucle.
    else:
        # El bucle for ha terminado con normalidad
        # El número que estábamos comprobando es primo
        primos.append(numero)  # Si no esta en la lista lo agragamos

print(str(primos))
