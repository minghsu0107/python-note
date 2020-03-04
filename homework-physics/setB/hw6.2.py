import math
import matplotlib.pyplot as plt
from pylab import *
import numpy as np

V0 = 1
freq = 6000*math.pi
R = 5
C = 10e-6
L = 200e-6

X = np.array([[0], [0]])
M = np.array([[0, 1.], [-1/(L*C), -R/L]])

Q = []
I = []
T = []

PR = []
PC = []
PL = []

dt = 1e-7
t = 0
last_i = 0
for k in range(10000):
	q = X[0][0]
	i = X[1][0]

	Q.append(q)
	I.append(i)
	T.append(t)

	PR.append(i*i*R)
	PC.append(i*q/C)
	PL.append(i*L*(i - last_i)/dt)

	E = np.array([[0], [V0 * math.sin(freq*t)/L]])
	dX = M.dot(X) + E
	X = X + dX * dt

	t = t + dt
	last_i = i
plt.plot(T, PR, label = 'PR(t)')
plt.plot(T, PC, label = 'PC(t)')
plt.plot(T, PL, label = 'PL(t)')
legend(loc = 'lower right')
plt.show()




