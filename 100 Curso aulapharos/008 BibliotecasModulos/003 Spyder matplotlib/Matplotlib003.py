import numpy as np 
import matplotlib.pyplot as plt 
x=np.linspace(-np.pi*2,np.pi*2,200) 
coseno=np.cos(x) 
seno=np.sin(x) 
plt.title("Funciones seno y coseno") 
plt.xlabel('Eje x') 
plt.ylabel('Eje y') 
plt.grid() 
plt.plot(x,coseno) 
plt.plot(x,seno) 
 