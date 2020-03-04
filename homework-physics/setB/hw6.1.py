import math
import matplotlib.pyplot as plt
from pylab import *
import numpy as np

V0 = 1
freq = 6000*math.pi
R = 5
C = 1e-5
L = 200*1e-6

X = np.array([[0], [0]])
M = np.array([[0, 1.0], [-1/(L*C), -R/L]])

Q = []
I = []
V = []
T = []

dt = 1e-7
t = 0

for i in range(10000):
	Q.append(X[0][0])
	I.append(X[1][0])
	T.append(t)

	v = V0 * math.sin(freq*t)
	V.append(v)

	E = np.array([[0], [v/L]])
	X = X + (M.dot(X) + E) * dt

	t = t + dt

plt.plot(T, I, label = 'I(t)')
legend(loc = 'lower right')
plt.show()

plt.plot(T, Q, label = 'Q(t)')
legend(loc = 'lower right')
plt.show()

plt.plot(T, V, label = 'V(t)')
legend(loc = 'lower right')
plt.show()

P = list(map(lambda x, y: x * y, I, V))

plt.plot(T, P, label = 'P(t)')
legend(loc = 'lower right')
plt.show()





