import numpy as np 
import matplotlib.pyplot as plt 
x=np.random.rand(40)*10 
numero_barras = 6 
plt.hist(x, numero_barras) 
plt.show()