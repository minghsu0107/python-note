import math
import matplotlib.pyplot as plt
from pylab import *
import numpy as np

class g:
	V0 = 1
	freq = 6000*math.pi
	R = 5
	C = 10e-6
	L = 200e-6
	dt = 1e-7

	def compute():	
		X = np.array([[0], [0]])
		M = np.array([[0, 1.], [-1/(g.L*g.C), -g.R/g.L]])

		Q = []
		I = []
		V = []
		T = []

		PR = []
		PC = []
		PL = []

		t = 0
		last_i = 0

		for k in range(10000):
			q = X[0][0]
			i = X[1][0]

			Q.append(q)
			I.append(i)
			T.append(t)

			PR.append(i*i*g.R)
			PC.append(i*q/g.C)
			PL.append(i*g.L*(i - last_i)/g.dt)

			v = math.sin(g.freq*t)
			V.append(v)
			E = np.array([[0], [g.V0 * v/g.L]])
			dX = M.dot(X) + E
			X = X + dX * g.dt

			t = t + g.dt
			last_i = i

		P = list(map(lambda x, y: x * y, I, V))
		return Q, I, V, T, PR, PC, PL, P

class demo:
	def __init__(self, mode = 0):
		self.Q, self.I, self.V, self.T, self.PR, self.PC, self.PL, self.P = g.compute()
		self.mode = mode
		self.fig = plt.figure()
		if mode == 0:
			self.ax = self.fig.add_subplot(2, 2, 1)
		else:
			self.ax = self.fig.add_subplot(111)

	def show_I(self):
		self.ax.plot(self.T, self.I, label = 'I(t)')
		self.ax.set_xlabel('t (sec)')
		self.ax.set_ylabel('I (A)', rotation=90)
		self.ax.legend(loc = 'lower right')		

	def show_Q(self):
		self.ax.plot(self.T, self.Q, label = 'Q(t)')
		self.ax.set_xlabel('t(sec)')
		self.ax.set_ylabel(r'Q (C)', rotation=90)
		self.ax.legend(loc = 'lower right')

	def show_p_rlc(self):
		self.ax.plot(self.T, self.PR, label = '$P_{R}(t)$')
		self.ax.plot(self.T, self.PC, label = '$P_{C}(t)$')
		self.ax.plot(self.T, self.PL, label = '$P_{L}(t)$')
		self.ax.axhline(y=0, color='k', linewidth=1)
		self.ax.set_xlabel('t (sec)')
		self.ax.set_ylabel('P (W)', rotation=90)
		self.ax.legend(loc = 'lower right')

	def show_p_total(self):
		self.ax.plot(self.T, self.P, label = 'P(t)')
		self.ax.set_xlabel('t (sec)')
		self.ax.set_ylabel('P (W)', rotation=90)
		self.ax.legend(loc = 'lower right')
		
	def show_all(self):
		self.show_I()
		self.ax = self.fig.add_subplot(2, 2, 2)
		self.show_Q()
		self.ax = self.fig.add_subplot(2, 2, 3)
		self.show_p_rlc()
		self.ax = self.fig.add_subplot(2, 2, 4)
		self.show_p_total()	

	def show_IV(self):
		ax2 = self.ax.twinx()
		self.ax.plot(self.T, self.I, label = 'I(t)', color='tab:blue')
		ax2.plot(self.T, self.V, label = 'V(t)', color='tab:orange')

		self.ax.set_xlabel('t (sec)')
		self.ax.set_ylabel('V (volt)', rotation=90)
		ax2.set_ylabel('I (A)', rotation=90)

		self.ax.legend(loc = 'upper left')
		ax2.legend(loc = 'upper right')

	def get_phase(self):
		t_I = -1
		t_V = -1
		for i in range(len(self.T)):
			if self.I[i] - 0 < 1e-7:
				t_I = self.T[i]
			if self.V[i] - 0 < 1e-7:
				t_V = self.T[i]

		return g.freq * (t_V - t_I)

	def show_result(self):
		if 0 <= self.mode and self.mode <= 5:
			if self.mode == 0:
				self.show_all()
			elif self.mode == 1:
				self.showI()
			elif self.mode == 2:
				self.show_Q()
			elif self.mode == 3:
				self.show_p_rlc()
			elif self.mode == 4:
				self.show_p_total()
			elif self.mode == 5:
				self.show_IV()
				print(self.get_phase())
			plt.show()
		else:
			print("invalid input.")

if __name__ == '__main__':

	t = demo(5)
	t.show_result()

	t2 = demo()
	t2.show_result()