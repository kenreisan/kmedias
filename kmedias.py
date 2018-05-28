import numpy as np


def test():
	a = np.matrix('1,2;3,5')

	a = a*a

	print(a)

	print(a[0,0])

test()