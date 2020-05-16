resistencias = {"probeta1":31.3, "probeta2":30.5, "probeta3":29.9, "probeta4":30.9} 
def calcular_media(diccionario): 
    acumulado = 0 
    for clave in diccionario: 
       acumulado = acumulado + diccionario[clave] 
    media = acumulado / len(diccionario) 
    return media 
resultado = calcular_media(resistencias) 
print("La media de resistencia de las probetas es", resultado)