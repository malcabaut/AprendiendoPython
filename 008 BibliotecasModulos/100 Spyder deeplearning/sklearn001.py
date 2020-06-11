#Voy a crear un csv con operaciones matematicas
#Con learn voy a intentar que resuelva las operaciones

from sklearn import metrics 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
import pandas as pd 
###################################
from random import randint
fichero = open ("fichero.csv", "w", encoding="utf-8")
fichero.write("num1,num2,result\n")
for i in range(100000):
    num1=randint(7,100)
    num2=randint(7,100)
    result=num1+num2
    fichero.write(str(num1)+","+str(num2)+","+str(result)+"\n")
fichero.close()
###################################
Datos = pd.read_csv('fichero.csv') 
X = Datos[['num1', 'num2']] 
Y = Datos['result']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4) 
lm = LinearRegression() 
lm.fit(X_train,Y_train)
coeficientes= pd.DataFrame(lm.coef_,X.columns,columns=['result']) 
print(coeficientes) 
predicciones = lm.predict(X_test) 
plt.scatter(Y_test,predicciones) 
print('MAE:', metrics.mean_absolute_error(Y_test, predicciones)) 
print('MSE:', metrics.mean_squared_error(Y_test, predicciones))
print('RMSE:', np.sqrt(metrics.mean_squared_error(Y_test, predicciones))) 