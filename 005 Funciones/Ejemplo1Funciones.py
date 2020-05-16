terminamos = 0 
#Creo mi función 
def funcionSuma(): 
    #Pregunto los números a sumar 
    numero1 = input("Primer numero: ") 
    numero2 = input("Segundo numero: ") 
    #Los convierto en entero: 
    numero1 = int(numero1) 
    numero2 = int(numero2) 
    #Sumo los números y los imprimo 
    suma = numero1+numero2 
    print("La suma de los dos números es",suma) 
    
while terminamos == 0: 
    print("Nuestras opciones:") 
    print("1. Realizar una suma") 
    print("2. Terminar") 
    pregunta = input("¿Qué quieres hacer? (1 o 2): ") 
    if pregunta == "1": 
        #Llamo a la función 
        funcionSuma() 
    elif pregunta == "2": 
        print ("Adiós") 
        terminamos = 1 