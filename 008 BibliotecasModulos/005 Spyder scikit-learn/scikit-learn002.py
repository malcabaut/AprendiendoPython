import seaborn as sns 
import pandas as pd 
import numpy as np 
USAhousing = pd.read_csv('USA_Housing.csv') 
sns.pairplot(USAhousing) 