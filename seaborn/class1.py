import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("diamonds")
#print(database)

#bins : How big you want your graph to be
sb.distplot(database["carat"],bins=1)

plt.show()