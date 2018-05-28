import numpy as np

def test():
	a = np.matrix([[1],[1]])
	b = np.matrix('2;1')
	c = np.matrix('4;3')
	d = np.matrix('5;4')

	d = np.matrix('0,0,0,0')

	print(d)

	q=2
	w=3
	r=4
	t=5
	d = np.matrix([[q,w,r,t]])

	print(d)

	d[0,3] = 20

	print(d)

	print(np.size(a))

	for x in d:
		print(x[0,0])

if __name__ == '__main__':
	test()