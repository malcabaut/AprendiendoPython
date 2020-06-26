terminamos = 0 
def funcionSuma(): 
    numero1 = input("Primer numero: ") 
    numero2 = input("Segundo numero: ") 
    numero1 = int(numero1) 
    numero2 = int(numero2) 
    #Devuelvo la suma de los números 
    return numero1 + numero2, numero1, numero2 
while terminamos == 0: 
    print("Nuestras opciones:") 
    print("1. Realizar una suma") 
    print("2. Terminar") 
    pregunta = input("¿Qué quieres hacer? (1 o 2): ") 
    if pregunta == "1": 
        suma = funcionSuma()
        print(suma)
    elif pregunta == "2": 
        print(suma) 
        print("Adiós") 
        terminamos = 1 