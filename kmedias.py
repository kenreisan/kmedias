import math
import numpy as np

def test():
	a = np.matrix('1,1;2,1;4,3;5,4')
	m1 = np.matrix('1,1;2,1')
	d = np.matrix('0.0,0.0,0.0,0.0;0.0,0.0,0.0,0.0')

	d[0,3] = 20

	for i in range(0,np.shape(d)[0]):
		for j in range(0,np.shape(d)[1]):
			d[i,j] = math.sqrt(float(((float(a[j,0]) - float(m1[i,0]))**2 + (float(a[j,1]) - float(m1[i,1]))**2)))
			#print(float(d[i,j]))

	print(d)

if __name__ == '__main__':
	test()