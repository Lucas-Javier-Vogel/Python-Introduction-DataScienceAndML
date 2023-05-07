import matplotlib.pyplot as plt
from matplotlib.pyplot import style

style.use("classic")

food = ["pizza","ice cream","burgers"]
sales = [200,100,300]
color = ["red","blue","green"]

plt.pie(sales,labels=food,colors=color)

plt.title("example food")

plt.show()