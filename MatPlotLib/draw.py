import matplotlib.pyplot as plt
listx = [1, 5, 7, 9, 13, 16]
listy = [15, 50, 80, 40, 70, 50]

# ls or linestyle: "-", "--", "-.", ":"
plt.plot(listx, listy, color="red", lw="5.0", ls="--", label="food")
plt.legend()
plt.show()

listx = [1, 5, 7, 9, 13, 16]
listy = [15, 50, 80, 40, 70, 50]
listx1 = [2, 6, 8, 11, 14, 16]
listy1 = [10, 40, 30, 50, 80, 60]
plt.plot(listx, listy)
plt.plot(listx1, listy1)
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.72, 0.72, 0.16, 0.16])
plt.show()
