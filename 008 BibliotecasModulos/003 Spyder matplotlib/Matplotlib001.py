import matplotlib.pyplot as plt 
plt.rcdefaults() 
dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes") 
posiciones = range(len(dias)) 
visitantes = [18,21,12,34,42] 
plt.bar(posiciones, visitantes, align='center') 
plt.xticks(posiciones, dias) 
plt.ylabel("Visitantes") 
plt.title("Numero de visitantes por dia") 
plt.show()