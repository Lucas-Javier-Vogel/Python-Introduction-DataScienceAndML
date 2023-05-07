import numpy as np

#random number from the first value to the second 
#value the times of the third value
#var1 = np.linspace(10,50,100)

var1 = np.array([(2,4,6),(1,3,5),(7,25,51),(10,33,65)])

#specific value
#print(var1[0,1])

#specific value in each line (the first indicates
#from what line and the second the specific value)
#print(var1[1:,1])

#max in the array
print(var1.max())
#min in the array
print(var1.min())
#sum of all the values in the array
print(var1.sum())