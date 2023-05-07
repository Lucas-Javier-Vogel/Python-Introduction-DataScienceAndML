import numpy as np

var1 = np.array([(2,4,6),(1,3,5)])
var2 = np.array([(2,4,6),(1,3,5)])

#Basic operations
#print(var1+var2)
#print(var1-var2)
#print(var1*var2)
#print(var1/var2)

#put all the values in the same column
#print(var1.ravel())

#With axis you select if the numbers are sum
#in column form or line form (y=0,x=1)
#print(var1.sum(axis=1))

print(np.sqrt(var1))