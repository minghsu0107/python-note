import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# x from 0 to 30
x = 30 * np.random.random((20, 1))
print(x.shape)  # (20, 1)
# y = a*x + b with noise
# np.random.randn(size) == np.random.normal(loc=0, scale=1, size)
# (μ=0, σ=1)
y = 0.5 * x + 1.0 + np.random.normal(size=x.shape)

# create a linear regression model
model = LinearRegression()
model.fit(x, y)

# predict y from the data
x_new = np.linspace(0, 30, 100)

y_new = model.predict(x_new[:, np.newaxis])  # np.newaxis == none
print(x_new[:, np.newaxis].shape)  # (100, 1)


# plot the results
plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')


plt.show()
