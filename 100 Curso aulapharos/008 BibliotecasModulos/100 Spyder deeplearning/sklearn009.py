import numpy as np 
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt
X=np.random.rand(400,2)*100
pca = PCA(n_components=2) 
pca=pca.fit_transform(X) 
plt.figure(1) 
plt.scatter(X[:, 0], X[:, 1]) 
plt.title("Original") 
plt.show 
plt.figure(2) 
plt.scatter(pca[:, 0], pca[:, 1]) 
plt.title("Con PCA") 
plt.show 