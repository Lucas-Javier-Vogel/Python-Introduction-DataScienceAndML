import matplotlib.pyplot as plt
from matplotlib.pyplot import style

style.use("bmh")

numbers = [1,29,30,12,52,75,13,78,9,23,14,75,98,13,77,93,56,72]
jumps = [0,15,30,45,60,75,90,105]

plt.title("test 1 hist")
plt.xlabel("test x label")
plt.ylabel("test y label")

plt.hist(numbers,jumps,histtype="bar")
#plt.hist(numbers,jumps,histtype="step")

plt.show()