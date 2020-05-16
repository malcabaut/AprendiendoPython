def media(*numeros): # puede introducir variables si saber el numero exacto.
   acumulado = 0 
   for numero in numeros: 
      #Recorro el arbitrario y voy almacenando el valor acumulado 
      acumulado = acumulado + numero 
   """Divido la suma de todos los números que contiene el arbitrario entre su longitud""" 
   media = acumulado/len(numeros) 
   return media 
#Aplico la función a unos números concretos 
miMedia = media(5,7,9,1,2,8) 
print("La media es", miMedia) 