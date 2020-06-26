# Sumando 2 numeros
numero1 = input("Introduce un numero1: ")
numero2 = input("Introduce un numero2: ")
# Cuando metemos numero no hay problema pero como intentes meter letras ...
try:
    print("La suma de "+numero1+"+"+numero2+"="
          + str(int(numero1) + int(numero2))) #si numero es un str falla.
except:
    print("Seguro que todos son numeros")
else:
    print("Todo correcto")
