import scipy as sp
import numpy as np
from scipy import linalg

array1 = np.array(([1,3],[2,4]))
array2 = np.array(([5,9],[6,8]))

print(linalg.solve(array1,array2))

function1 = linalg.inv(array1)

print(function1)