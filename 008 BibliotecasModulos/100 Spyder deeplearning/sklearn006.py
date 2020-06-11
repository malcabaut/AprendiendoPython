from sklearn import linear_model 
X=[[0, 0], [2, 2]] 
y=[0.5, 2.5] 
reg = linear_model.Ridge() 
reg.fit(X, y)  
print(reg.predict([[1,1]]))