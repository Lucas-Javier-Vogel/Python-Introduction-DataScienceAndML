import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets._samples_generator import make_blobs

x,y_true=make_blobs(n_samples=800,centers=5,cluster_std=0.45,random_state=0)

plt.scatter(x[:,0],x[:,1],s=30)

func1 = KMeans(n_clusters=4)
func1.fit(x)
y_func = func1.predict(x)

plt.scatter(x[:,0],x[:,1],c=y_func,s=15)
centers = func1.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c="red",s=75,alpha=1)

plt.show()
