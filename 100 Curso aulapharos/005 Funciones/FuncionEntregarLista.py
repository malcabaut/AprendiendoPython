numeros = [1,5,6,3,6,4] 
def calcular_media(lista): 
    acumulado = 0 
    for i in lista: 
       acumulado = acumulado + i 
    media = acumulado / len(lista) 
    return media 
resultado = calcular_media(numeros) 
print("La media ", numeros, "es", resultado) 