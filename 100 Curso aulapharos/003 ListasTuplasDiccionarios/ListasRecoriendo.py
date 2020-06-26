notas = [4, 3, 2, 7, 1, 8, 5, 10, 3, 8,0,0] 
suspensos = 0 
aprobados = 0 
for nota in notas: 
   if nota < 5: 
      suspensos = suspensos + 1 
   elif nota >= 5: 
      aprobados += 1 
print ("Hay",suspensos,"suspensos.") 
print ("Hay",aprobados,"aprobados.")