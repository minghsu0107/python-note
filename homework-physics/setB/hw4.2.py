import numpy as np
# assume that v0 = 0 (reference)
# Compute the matrix for the circuit layouts
def readInput():
	m = int(input("please enter the number of circuit layouts\n")) 
	bat_cnt = 0
	arr = np.loadtxt('hw4.txt', delimiter = ' ')
	# np.savetxt('hw4.txt', arr)
	d = dict()
	for i in range(m):
		for j in range(4):
			if (j == 0 or j == 1):
				if (arr[i][j] not in d.keys()):
					d[arr[i][j]] = True
			elif (j == 2 and arr[i][j] == 0):
				bat_cnt += 1
	return arr, bat_cnt, len(d), m
def isBattery(flag):
	if (not flag):
		return True
	return False
def getMatrix(arr, bat_cnt, n, m):
	coef = np.zeros([n + bat_cnt - 1, n + bat_cnt - 1])
	val = np.zeros([n + bat_cnt - 1, 1])
	idx = n - 1
	for i in range(m):
		va = int(arr[i][0])
		vb = int(arr[i][1])
		d = arr[i][3] # d = voltage if isBattery, else d = resistance 
		if (isBattery(arr[i][2])):
			val[idx][0] = d
			if (va == 1):
				# 0 - vb = d, -vb = d
				coef[idx][vb - 2] += -1
				# for node vb, I_battery -= Iab
				coef[vb - 2][idx] += -1
			else:
				# va - vb = d
				coef[idx][va - 2] += 1 
				coef[idx][vb - 2] -= 1
				# for node va, I_battery += Iab
				coef[va - 2][idx] += 1
				# for node vb, I_battery -= Iab
				coef[vb - 2][idx] -= 1
			idx += 1
		else:
			if (va == 1):
				# for node vb, I_resistor -= (0 - vb)/d
				coef[vb - 2][vb - 2] += 1/d
			else:
				# for node va, I_resistor += (va - vb)/d
				coef[va - 2][va - 2] += 1/d
				coef[va - 2][vb - 2] -= 1/d
				# for node vb, I_resistor -= (va - vb)/d
				coef[vb - 2][va - 2] -= 1/d
				coef[vb - 2][vb - 2] += 1/d
	return coef, val		
def getAns(mat1, mat2):
	#mat1 = np.array(mat1)
	#mat2 = np.array(mat2)
	return np.linalg.inv(mat1).dot(mat2)
if __name__ == '__main__':
	arr, bat_cnt, n, m = readInput()
	mat1, mat2 = getMatrix(arr, bat_cnt, n, m)
	print(np.around(getAns(mat1, mat2), decimals=2))