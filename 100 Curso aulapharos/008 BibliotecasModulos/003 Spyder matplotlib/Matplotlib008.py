import numpy as np 
import matplotlib.pyplot as plt 

x=np.random.rand(80) 
y=np.random.rand(80) 

plt.scatter(x,y, c=range(80)) 
plt.show() 

plt.figure(1)
plt.scatter(X_test[:, 0], X_test[:, 1]) 
plt.show()
 
