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
Q1 = []
Q2 = []
Q3 = []
T = []
x1 = 0
x2 = 0
x3 = 0
v1 = 0.2
v2 = -0.2
v3 = 0.2
t = 0
dt = 0.0001
while t < 10:
    Q1.append(x1 + 2 * x2 + x3)
    Q2.append(x1 - x3)
    Q3.append(x1 - 2 * x2 + x3)
    X1.append(x1)
    X2.append(x2)
    X3.append(x3)
    T.append(t)
    a1 = -k * (x1 - x2)/m1
    a2 = (-k * (x2 - x1) + k * (x3 - x2))/m2
    a3 = -k * (x3 - x2)/m3
    x1 = x1 + v1 * dt
    x2 = x2 + v2 * dt
    x3 = x3 + v3 * dt
    v1 = v1 + a1 * dt
    v2 = v2 + a2 * dt
    v3 = v3 + a3 * dt
    t = t + dt
#plt.plot(T,X1,label = 'x1(t)')
#plt.plot(T,X2,label = 'x2(t)')
#plt.plot(T,X3,label = 'x3(t)')
plt.plot(T,Q1,label = 'q1(t)')
plt.plot(T,Q2,label = 'q2(t)')
plt.plot(T,Q3,label = 'q3(t)')
legend(loc = 'lower right')
plt.show()
