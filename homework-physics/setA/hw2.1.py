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
x0 = 0.01
x = x0
U0 = A*x0*x0*math.e**(-x0*x0/B)
Um = 0.7357458067142384
v1 = ((0.2*Um - U0)*2/m)**(1/2)
v2 = ((0.4*Um - U0)*2/m)**(1/2) 
v3 = ((0.6*Um - U0)*2/m)**(1/2) 
v4 = ((0.8*Um - U0)*2/m)**(1/2) 
v5 = ((Um - U0)*2/m)**(1/2)
v6 = ((1.2*Um - U0)*2/m)**(1/2) 
v7 = ((1.4*Um - U0)*2/m)**(1/2) 
X1 = []
X2 = []
X3 = []
X4 = []
X5 = []
X6 = []
X7 = []
V1 = []
V2 = []
V3 = []
V4 = []
V5 = []
V6 = []
V7 = []
while t < 10:
   X1.append(x)
   V1.append(v1)
   U = (A*x*x*math.e**(-x*x/B))
   a = -(2*U/x + U* (-2*x/B))/m
   x = x + v1 *dt
   v1 = v1 + a*dt
   t = t + dt
x = x0
t = 0
while t < 10:
   X2.append(x)
   V2.append(v2)
   U = (A*x*x*math.e**(-x*x/B))
   a = -(2*U/x + U* (-2*x/B))/m
   x = x + v2 *dt
   v2 = v2 + a*dt
   t = t + dt
x = x0
t = 0
while t < 10:
   X3.append(x)
   V3.append(v3)
   U = (A*x*x*math.e**(-x*x/B))
   a = -(2*U/x + U* (-2*x/B))/m
   x = x + v3 *dt
   v3 = v3 + a*dt
   t = t + dt
x = x0
t = 0
while t < 10:
   X4.append(x)
   V4.append(v4)
   U = (A*x*x*math.e**(-x*x/B))
   a = -(2*U/x + U* (-2*x/B))/m
   x = x + v4 *dt
   v4 = v4 + a*dt
   t = t + dt
x = x0
t = 0
while t < 10:
   if v5 < 0.1:
     break
   X5.append(x)
   V5.append(v5)
   U = (A*x*x*math.e**(-x*x/B))
   a = -(2*U/x + U* (-2*x/B))/m
   x = x + v5 *dt
   v5 = v5 + a*dt
   t = t + dt
x = x0
t = 0
while t < 10:
   X6.append(x)
   V6.append(v6)
   U = (A*x*x*math.e**(-x*x/B))
   a = -(2*U/x + U* (-2*x/B))/m
   x = x + v6 *dt
   v6 = v6 + a*dt
   t = t + dt
x = x0
t = 0
while t < 10:
   X7.append(x)
   V7.append(v7)
   U = (A*x*x*math.e**(-x*x/B))
   a = -(2*U/x + U* (-2*x/B))/m
   x = x + v7 *dt
   v7 = v7 + a*dt
   t = t + dt
plt.plot(X1,V1,label = 'E = 0.2Um')
plt.plot(X2,V2,label = 'E = 0.4Um')
plt.plot(X3,V3,label = 'E = 0.6Um')
plt.plot(X4,V4,label = 'E = 0.8Um')
plt.plot(X5,V5,label = 'E = 1Um')
plt.plot(X6,V6,label = 'E = 1.2Um')
plt.plot(X7,V7,label = 'E = 1.4Um')
legend(loc = 'lower right')
plt.show()
