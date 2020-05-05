repetimos = True
while repetimos == True:
    try:
        numero = float(input("Dime un número: "))
        repetimos = False
    except:
        print("Seguro que es un numero")