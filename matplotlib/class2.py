import matplotlib.pyplot as plt
from matplotlib.pyplot import style

style.use("bmh")

x1=[2,4,6]
y1=[3,6,9]

x2=[4,8,12]
y2=[5,10,15]

x3=[6,12,18]
y3=[12,24,36]

plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)

plt.title("test graph 1")
plt.xlabel("test x name")
plt.ylabel("test y name")

plt.show()