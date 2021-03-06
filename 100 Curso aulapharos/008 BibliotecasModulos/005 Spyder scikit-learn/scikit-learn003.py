import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
import pandas as pd 
USAhousing = pd.read_csv('USA_Housing.csv') 
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']] 
Y = USAhousing['Price'] 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4) 
lm = LinearRegression() 
lm.fit(X_train,Y_train) 
coeficientes= pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient']) 
print(coeficientes) 
predictions = lm.predict(X_test) 
plt.scatter(Y_test,predictions)