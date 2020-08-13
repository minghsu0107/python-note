import numpy as np
import matplotlib.pyplot as plt

labels = ["a", "b", "c", "d"]
sizes = [5, 10, 20, 15]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.05, 0)
plt.pie(sizes, explode=explode, labels=labels,
        colors=colors, labeldistance=1.1, autopct="%3.1f%%", shadow=True,
        startangle=90, pctdistance=0.6)
plt.axis("equal")
plt.show()


n = 10
Z = np.ones(n)

plt.axes([0.025, 0.025, 0.95, 0.95])  # down left, down right, width, height

plt.pie(Z, explode=Z*.05, colors=['%f' % (i/float(n)) for i in range(n)])
plt.axis('equal')
plt.xticks(())
plt.yticks()

plt.show()
