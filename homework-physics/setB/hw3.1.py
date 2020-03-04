from vpython import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

MAX = 32

class demo:
	def __init__(self, V1, V2, V3, V4):
		self.V1 = V1
		self.V2 = V2
		self.V3 = V3
		self.V4 = V4
		self.V = [[0 for j in range(MAX)] for i in range(MAX)]
		#self.Ex = [[0 for j in range(MAX)] for i in range(MAX)]
		#self.Ey = [[0 for j in range(MAX)] for i in range(MAX)]
		self.E = [[np.array([0,0],dtype=np.float32) for j in range(MAX)] for i in range(MAX)]
	def get_volt(self):
		for i in range(MAX):
		    for j in range(MAX):
		    	if i == 0 and j > 0 and j < MAX - 1:
		    		self.V[i][j] = self.V1
		    	elif i > 0 and i < MAX - 1 and j == MAX - 1:
		    		self.V[i][j] = self.V2
		    	elif i == MAX - 1 and j > 0 and j < MAX - 1:
		    		self.V[i][j] = self.V3
		    	elif i > 0 and i < MAX - 1 and j == 0:
		    		self.V[i][j] = self.V4
		for t in range(1000):
			for i in range(1, MAX - 1):
				for j in range(1, MAX - 1):
					avg = lambda i, j: (self.V[i-1][j] + self.V[i+1][j] + self.V[i][j-1] + self.V[i][j+1])/4.0
					self.V[i][j] = avg(i, j)
	def get_elc_field(self):
		for i in range(1, MAX - 1):
			for j in range(1, MAX - 1):
				#self.Ex[i][j] = (self.V[i-1][j] - self.V[i+1][j])/2.0
				#self.Ey[i][j] = (self.V[i][j-1] - self.V[i][j+1])/2.0
				self.E[i][j][0] = (self.V[i-1][j] - self.V[i+1][j])/2.0
				self.E[i][j][1] = (self.V[i][j-1] - self.V[i][j+1])/2.0
	def plot(self, elc = True):
		if elc:
			for i in range(1, MAX - 1):
				for j in range(1, MAX - 1):
					#pointer = arrow(pos=vector(i,j,0), axis=vector(self.Ex[i][j],self.Ey[i][j],0), shaftwidth=0)
					pointer = arrow(pos=vector(i,j,0), axis=vector(self.E[i][j][0],self.E[i][j][1],0), shaftwidth=0)
		else:
			fig = plt.figure()
			ax = fig.add_subplot(111, projection='3d')
			for i in range(MAX):
				for j in range(MAX):
					ax.scatter(i, j, self.V[i][j], c='b')
			ax.set_xlabel('X Label')
			ax.set_ylabel('Y Label')
			ax.set_zlabel('Z Label')
			 
			plt.show()
			
if __name__ == '__main__':
	field = demo(10, -20, -30, 0)
	field.get_volt()
	field.get_elc_field()
	field.plot()
	field.plot(elc = False)