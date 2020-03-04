import matplotlib.pyplot as plt

listx = [1, 5, 7, 9, 13 , 16]
listy = [15, 50, 80, 40, 70, 50]
listx1 = [2, 6, 8, 11, 14, 16]
listy1 = [10, 40, 30, 50, 80, 60]

plt.plot(listx, listy, label="Male")
plt.plot(listx1, listy1, color="red", linewidth=5,
	linestyle="--", label="Female")
plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title("Pocket Money")
plt.xlabel("Age")
plt.ylabel("Money")
plt.show()