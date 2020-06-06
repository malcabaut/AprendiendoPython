import numpy as np 
import matplotlib.pyplot as plt 
cantidad = 8000 
x=np.random.rand(cantidad) 
y=np.random.rand(cantidad) 
plt.scatter(x,y, c=range(cantidad)) 
plt.show() 