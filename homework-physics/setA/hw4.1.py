import math
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
k = 10
m1 = 1 
m2 = 2
m3 = 1
X1 = []
X2 = []
X3 = []
T = []
x1 = 0
x2 = 0
x3 = 0
v1 = 1
v2 = 1
v3 = 1
t = 0
dt = 0.0001
while t < 10:
    X1.append(x1)
    X2.append(x2)
    X3.append(x3)
    T.append(t)
    a1 = -k * (x1 - x2)/m1
    a2 = (-k * (x2 -x1) + k * (x3 - x2))/m2
    a3 = -k * (x3 - x2)/m3
    x1 = x1 + v1 * dt
    x2 = x2 + v2 * dt
    x3 = x3 + v3 * dt
    v1 = v1 + a1 * dt
    v2 = v2 + a2 * dt
    v3 = v3 + a3 * dt
    t = t + dt
plt.plot(T,X1,label = 'x1(t)')
plt.plot(T,X2,label = 'x2(t)')
plt.plot(T,X3,label = 'x3(t)')
legend(loc = 'lower right')
plt.show()
