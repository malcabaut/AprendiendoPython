def hormigon(): 
   cantidad = float(input("¿Cuántos metros cúbicos de hormigón quieres?:")) 
   cantidad_por_metro = [322,689,1177,156] 
   tipo_material = ["Cemento","Arena","Grava","Agua"] 
   materiales = {} 
   for i in tipo_material: 
     materiales[i] = cantidad_por_metro[tipo_material.index(i)]*cantidad 
   return materiales 
materiales = hormigon() 
print(materiales)