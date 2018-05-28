import math
import numpy as np

def test():
	a = np.matrix('1,1;2,1;4,3;5,4')
	d = np.matrix('0.0,0.0,0.0,0.0;0.0,0.0,0.0,0.0')
	m1 = np.matrix('1,1;2,1')
	m2 = np.matrix('.0,.0;.0,.0')
	g = [[],[]]
	gn= [[],[]]

	numero = 1

	d[0,3] = 20

	print("\nIteracion: " + str(numero))
	g = distancia(d,a,m1,g)

	numero += 1
	"""
	Hasta aqui funiona.. no se como calcular la siguiente media
	"""


	while (np.array_equal(g,gn) != True):

		for c in g[0]:
			m2[0,0] = c[0] + m2[0,0]
			m2[0,1] = c[1] + m2[0,1]
		m2[0,0] = m2[0,0]/len(g[0])
		m2[0,1] = m2[0,1]/len(g[0])
		#print(m2)

		for c in g[1]:
			m2[1,0] = c[0] + m2[1,0]
			m2[1,1] = c[1] + m2[1,1]
		m2[1,0] = m2[1,0]/len(g[1])
		m2[1,1] = m2[1,1]/len(g[1])
		#print(m2)

		print("\nIteracion: " + str(numero))
		gn = distancia(d,a,m2,gn)
		numero += 1

		if (np.array_equal(g,gn) != True):
			#print('salior esto')
			#print(g)
			#print(gn)
			g = gn
			#print('se igualan:')
			#print(g)
			m2 = np.matrix('.0,.0;.0,.0')
			gn = [[],[]]
			#print('valores')

def distancia(d,a,m1,g):

	for i in range(0,np.shape(d)[0]):
		for j in range(0,np.shape(d)[1]):
			d[i,j] = math.sqrt((a[j,0] - m1[i,0])**2 + (a[j,1] - m1[i,1])**2)
	print(d)

	for x in range(0,np.shape(d)[1]):
		if d[0,x] < d[1,x]:
			g[0].append([a[x,0],a[x,1]])
		else:
			g[1].append([a[x,0],a[x,1]])
	#print(g)
	#print(len(g[0]))
	#print(len(g[1]))

	return g


if __name__ == '__main__':
	test()