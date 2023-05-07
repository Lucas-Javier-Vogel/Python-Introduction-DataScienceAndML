import scipy as sp
from scipy import integrate as inte

#var1 = lambda x: x**3
#func1 = inte.quad(var1,0,6)

var1 = lambda y, x: x* y**4
func1 = inte.dblquad(var1,0,6,lambda x:0, lambda x:1)

print(func1)