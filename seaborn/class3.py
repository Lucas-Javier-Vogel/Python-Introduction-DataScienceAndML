import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("flights")
#print(database)
#box,strip,violin
sb.catplot(x="month",y="passengers",data=database,kind="box")

plt.show()