import numpy as np 
import matplotlib.pyplot as plt 
x=np.linspace(-np.pi*2,np.pi*2,200) 
y=np.cos(x) 
plt.title("Función coseno") 
plt.xlabel('Eje x') 
plt.ylabel('Eje y') 
plt.grid() 
plt.plot(x,y) 
 