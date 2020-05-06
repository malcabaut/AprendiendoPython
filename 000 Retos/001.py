# Reto propuesto por el curso que estoy siguiendo de Structuralia (https://sando.aulapharos.com/).
# Tema2 INPUT – OUTPUT Y VARIABLES
'''
Debes hacer un script que pregunte al usuario por dos números y los almacene (en diferentes variables). 
A continuación el programa deberá mostrarnos varias operaciones comentando primero qué operaciones ha realizado. 
Al menos debe realizar cinco operaciones con los números introducidos.
Los números introducidos pueden condicionar las operaciones por lo que se debe avisar de qué números no son válidos 

por ejemplo, no podemos realizar la raíz cuadrada de un número negativo o no se puede dividir entre cero.
'''
repetir = True #Variable para controlar el bucle y repetir mientras los datos introducido no sean numeros.
while repetir == True: #Comprobamos que la variable se correcta.
    try:#intentamos guardar en numero1 y numero2 float si no es posible la conversion da un fallo.
        numero1 = float(input("Dime un numero1: ")) #Solicitamos al usuario un numero y lo traformamos en un float.
        numero2 = float(input("Dime un numero2: "))
        repetir = False #si llega aqui todo va bien y el codigo continua.
    except:# en caso de que falle indicamos que tiene que introducir 2 numeros.
        print("Tiene que introducir 2 numeros")
print("Numero1: "+str(numero1))
print("Numero2: "+str(numero2))
# Nos piden que realizamos varias operaciones con estos numero.

# Suma
numero = numero1 + numero2
print(str(numero1)+" + "+str(numero2)+" = "+str(numero)+" --> SUMA")

# Resta
numero = numero1 - numero2
print(str(numero1)+" - "+str(numero2)+" = "+str(numero)+" --> RESTA")

# Multiplicación
numero = numero1 * numero2
print(str(numero1)+" * "+str(numero2)+" = "+str(numero)+" --> MULTIPLICACION")

# Potencia
numero = numero1 ** numero2
print(str(numero1)+" ^ "+str(numero2)+" = "+str(numero)+" --> POTENCIA")

# División
try:
    numero = numero1 / numero2
    print(str(numero1)+" / "+str(numero2)+" = "+str(numero)+" --> DIVISIÓN")
except:
    print("Intentado dividir por 0 bribón")

# Parte entera de una división
try:
    numero = numero1 // numero2
    print(str(numero1)+" // "+str(numero2)+" = "+str(numero)+" --> PARTE ENTERA")
except:
    print("Intentado dividir por 0 bribón")

# Resto de una división
try:
    numero = numero1 % numero2
    print(str(numero1)+" % "+str(numero2)+" = "+str(numero)+" --> RESTO")
except:
    print("Intentado dividir por 0 bribón")
<<<<<<< HEAD
=======

>>>>>>> 1b3ad7bfc8618d83f896bbe63fbbec72ade30157
