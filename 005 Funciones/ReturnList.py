def hormigon(): 
   cantidad = float(input("¿Cuántos metros cúbicos de hormigón quieres?:")) 
   cantidad_por_metro = [322,689,1177,156] 
   materiales = [] 
   for i in range(len(cantidad_por_metro)): 
       materiales.append(cantidad_por_metro[i]*cantidad) 
   return materiales 
materiales = hormigon() 
print(materiales) 