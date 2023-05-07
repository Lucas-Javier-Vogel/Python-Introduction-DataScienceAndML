import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import style

#x=np.array([1,2,6,4,7,8,9,21,4,32,3,5,6,2])
#y=np.array([10,12,16,14,17,18,19,31,6,11,38,15,4,27])

x=([1,2,3,4,5,6,7,8,9,10])
y=([1,4,5,3,5,29,1,13,17,26])
func1 = np.polyfit(x,y,1)

plt.plot(x,y,".")
plt.plot(x,np.polyval(func1,x),"-")

plt.show()