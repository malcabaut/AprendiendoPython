#Con bucles 
from random import sample 
import time  
start = time.time() 
a=sample(range(100000),k=100000) 
b=[] 
for i in a: 
    if i>0: 
        b.append(i) 
end= time.time() 
print("Tiempo empleado con bucle: ", end-start)

#Vectorizado 
import time 
import numpy as np 
start=time.time() 
a=np.random.rand(100000) 
b=np.delete(a,np.where(a<0)) 
end=time.time() 

print("Tiempo empleado vectorizado: ", end-start) 