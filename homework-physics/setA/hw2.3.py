import math
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
A = 1
B = 2
m = 1
max = -1
t = 0
dt = 0.0001
x0 = 0.1
x = x0
U0 = A*x*x*math.e**(-x*x/B)
Um = 0.7357458067142384
v = ((0.4*Um - U0)*2/m)**(1/2)
X = []
T = []
xmax = -100
xmin = 100
t1 = 0
t2 = 0
while t < 25:
   X.append(x)
   T.append(t)
   if x > xmax:
      xmax = x
      t1 = t
   if x < xmin:
      xmin = x
      t2 = t
   U = (A*x*x*math.e**(-x*x/B))
   a = -(2*U/x + U* (-2*x/B))/m
   x = x + v *dt
   v = v + a*dt
   t = t + dt
   flag = 1
print("The period is", (t2 - t1)*2 ,"s")
print("The amplitude is", (xmax - xmin)/2 ,"m")
plt.plot(T,X)
plt.show()
