from vpython import *
from random import random
import numpy as np

# physical parameter initialization
r = 0.02
L = 1.
N = 200
mHe = 4.E-3/6.02E23
kB = 1.38E-23
atoms = []
v_initial = 5.
T = mHe*(v_initial**2)/(3*kB)
# animation scene initialization
winsize = 500
scene = canvas(width = winsize, height = winsize)
scene.range = L
d = L/2 + r
borders_bot = curve(pos = [(d, -d, d), (-d, -d, d), (-d, -d, -d), (d, -d, -d), (d, -d, d)], radius = 0.005, color = color.white)
borders_top = curve(pos = [(d, d, d), (-d, d, d), (-d, d, -d), (d, d, -d), (d, d, d)], radius = 0.005, color = color.white)
borders_1 = curve(pos = [(d, -d, d), (d, d, d)], radius = 0.005, color = color.white)
borders_2 = curve(pos = [(d, -d, -d), (d, d, -d)], radius = 0.005, color = color.white)
borders_3 = curve(pos = [(-d, -d, d), (-d, d, d)], radius = 0.005, color = color.white)
borders_4 = curve(pos = [(-d, -d, -d), (-d, d, -d)], radius = 0.005, color = color.white)

# statistics graph initialization
deltav = 0.2    # bin size of the histogram
vbin = arange(-5, 5, deltav)    # stat range vx = -5 ~ 5
stat_graph = graph(width = winsize, height = 0.6 * winsize, xmin = -5, xmax = 5, ymax = 16, xtitle = 'vx (m/s)', ytitle = 'dN')
theory = gcurve(color = color.cyan)
observation = gvbars(color = color.red, delta = deltav)

# bookkeeping atom position and velocity
X = np.zeros(shape = (N, 3))
V = np.zeros(shape = (N, 3))

# object initialization
for i in range(N):
    xi = L*random() - L/2 
    yi = L*random() - L/2
    zi = L*random() - L/2
    atoms.append(sphere(pos = vector(xi, yi, zi), radius = r, color = color.blue))
    X[i] = np.array([xi, yi, zi])
    V[i] = np.array([v_initial, 0., 0.]) 

def dN(u):
    return N*deltav*sqrt(mHe/(2*pi*kB*T))*exp(-0.5*mHe*u*u/(kB*T))
du = 0.01
for u in arange(-5., 5., du):
    theory.plot(pos=(u, dN(u)))
    continue


# time evolution
t = 0
dt = 0.01

F  = 0
def collision(i, j, sum):
    vi = V[i]-(np.dot(V[i]-V[j],X[i]-X[j])/sum**2)*(X[i]-X[j])
    vj = V[j]-(np.dot(V[j]-V[i],X[j]-X[i])/sum**2)*(X[j]-X[i])
    return vi, vj
while t < 20:
    rate(1/dt)
    t += dt
    U = 0
    for i in range(N):
        U += 0.5*mHe*np.dot(V[i], V[i])
    # plot and update the histogram of vx
    vx_hist = np.histogram(V[:, 0], bins = vbin)[0]
    observation.delete()
    for i in range(len(vx_hist)):
        observation.plot(vbin[i]+0.5*deltav, vx_hist[i])

    for i in range(N - 1):
        for j in range(i+1, N):
            sum = 0.
            for k in range(3):
                sum += (X[i][k] - X[j][k])**2
            sum = sqrt(sum)
            if sum <= 2*r and np.dot(V[i] - V[j], X[i] - X[j]) < 0:
               V[i], V[j] = collision(i, j, sum)
    for i in range(N):
        for k in range(3):
            if (abs(X[i][k]) + r >= L/2) and X[i][k]*V[i][k] > 0:
               V[i][k] = -V[i][k]
    for i in range(N):
        if abs(X[i][0]) + r >= L/2:
            F += abs(2*mHe*V[i][0]) / dt
    # step forward by dt by X=X+V*dt and update the new positions
    for i in range(N):
        X[i] = X[i] + V[i] * dt
        atoms[i].pos.x = X[i][0]
        atoms[i].pos.y = X[i][1]
        atoms[i].pos.z = X[i][2]
print("F: ",F/dt)
print("Pressure: ",F/dt/L**2)