import matplotlib.pyplot as plt
import numpy as np

# linspace(start, stop, 21) returns a list
# with 21 equidistant numbers in [start, stop]
x = np.linspace(0, 10, 21)
plt.plot(x, x, 'r^')
plt.plot(x, x**2, '--')
plt.plot(x, x**3, 'go')

plt.show()


x = np.linspace(0, 5, 21)
plt.figure()

plt.subplot(231)
plt.plot(x, x)

plt.subplot(232)
plt.plot(x, x**2)

plt.subplot(233)
plt.plot(x, x**3)

plt.subplot(234)
plt.plot(x, x**0.5)

plt.subplot(235)
plt.plot(x, x**0.25)

plt.subplot(236)
plt.plot(x, x*2)

plt.show()
