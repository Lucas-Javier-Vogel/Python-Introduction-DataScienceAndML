import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("tips")
#print(database)

graph = sb.FacetGrid(database,col="sex",hue="smoker")
graph.map(plt.scatter,"total_bill","tip")

plt.show()