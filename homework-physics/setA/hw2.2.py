import math
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
A = 1
B = 2
max = -1
x = np.arange(-12, 12, 0.01)
y = (A*x*x*math.e**(-x*x/B))
y1 = -(2*y/x + y* (-2*x/B))
plt.plot(x,y,label = 'U(x)')
plt.plot(x,y1,label = 'F(x)')
legend(loc = 'upper left')
for x in arange(-12, 12, 0.01):
    y = A*x*x*math.e**(-x*x/B)
    if y > max:
        max = y;
        pos_x = x
print("The maximum potential energy is", max ,"J")
print("In this moment, x =", pos_x ,"and", -pos_x, "m")
plt.show()
