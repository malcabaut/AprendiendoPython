import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap 
from sklearn import svm 
from sklearn.model_selection import train_test_split 
import numpy as np 
X=(np.random.rand(800,2)*100).astype(int) 
y=np.zeros(800) 
y[np.where((X[:,0]>20)&(X[:,1]<40))]=1 
y[np.where((X[:,0]<20)&(X[:,1]>60))]=1 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 
clf = svm.SVC() 
clf = svm.SVC(gamma=0.001, C=100) 
clf.fit(X_train, y_train) 
prediccion = clf.predict(X_test) 
plt.figure(1) 
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test) 
plt.title("Real") 
plt.show() 
plt.figure(2) 
plt.scatter(X_test[:, 0], X_test[:, 1], c=prediccion) 
plt.title("Predecido sobre set de testeo") 
plt.show()