import matplotlib.pyplot as plt
from matplotlib.pyplot import style

style.use("bmh")

x=[3,6,7,9,10]
y=[5,10,25,3,1]

plt.title("text scatter")
plt.xlabel("text x")
plt.ylabel("text y")

plt.scatter(x,y)

plt.show()