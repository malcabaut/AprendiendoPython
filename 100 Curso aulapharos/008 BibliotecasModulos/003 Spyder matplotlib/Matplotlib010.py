import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
cantidad= 100
x=np.random.rand(cantidad) 
y=np.random.rand(cantidad) 
z=np.random.rand(cantidad) 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
ax.scatter(x,y,z) 
ax.view_init(30, 30) 
plt.show()