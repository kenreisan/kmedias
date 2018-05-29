# -*- coding: utf-8 *-*

"""
Romero Hurtado Eduardo David

VERSION 0.6
28 MAYO 2018

Programa de agrupamiento K-medias.

El programa esta en una etapa muy preeliminar y solo funciona con k=2,
es decir que solo hace agrupamientos con 2 medias. 
Falta optimizarlo y mejorar el codigo que esta muy feo.
"""

import math
import numpy as np

def kmedia():
	"""Algoritmo de agrupamiento k-medias.

	Agrupa los puntos dependiendo del centroide mas cercano.
	Datos:	a = matriz de puntos.
			m1= matriz de medias (centroides).
			d = matriz vacia donde se almacenan las distancias de
				cada pto. a cada centroide.
			g = lista con los grupos creados.

	Tanto <m2> como <gn> se utilizan para el recalculo de medias y
	la nueva lista de grupos de puntos.
	"""

	a = np.matrix('1,1;2,1;4,3;5,4')
	m1 = np.matrix('1,1;2,1')
	d = np.matrix('0.0,0.0,0.0,0.0 ; 0.0,0.0,0.0,0.0')

	#a = np.matrix('8,10;3,10.5;7,13.5;5,18;5,13;6,9;9,11;3,18;8.5,12;8,16')
	#d = np.matrix('0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0 ; 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0')
	#m1 = np.matrix('8,10;5,13')
	
	m2 = np.matrix('0.0,0.0 ; 0.0,0.0')
	g = [[],[]]
	gn= [[],[]]

	numero = 1

	print('\nITERACION: ' + str(numero) + '\n')
	g = distancia(d,a,m1,g)
	print('puntos pertenecientes a ' + str(m1[0]) + ':\n' + str(g[0]))
	print('puntos pertenecientes a ' + str(m1[1]) + ':\n' + str(g[1]))

	numero += 1

	while (np.array_equal(g,gn) != True):

		for c in g[0]:
			m2[0,0] = c[0] + m2[0,0]
			m2[0,1] = c[1] + m2[0,1]
		m2[0,0] = m2[0,0]/len(g[0])
		m2[0,1] = m2[0,1]/len(g[0])

		for c in g[1]:
			m2[1,0] = c[0] + m2[1,0]
			m2[1,1] = c[1] + m2[1,1]
		m2[1,0] = m2[1,0]/len(g[1])
		m2[1,1] = m2[1,1]/len(g[1])

		print('\nNueva medias:\n' + str(m2))

		print('\nITERACION: ' + str(numero) + '\n')
		gn = distancia(d,a,m2,gn)
		print('puntos pertenecientes a ' + str(m2[0]) + ':\n' + str(gn[0]))
		print('puntos pertenecientes a ' + str(m2[1]) + ':\n' + str(gn[1]))
		numero += 1

		if (np.array_equal(g,gn) != True):
			g = gn
			m2 = np.matrix('.0,.0;.0,.0')
			gn = [[],[]]

def distancia(d,a,m1,g):
	"""Calcula la dist. eclidiana de cada pto. a cada centroide.

	Recibe: d = matriz vacia donde se almacenaran las dist.
			a = matriz de puntos a agrupar.
			m1= matriz de las medias.
			g = tupla donde se agrupan los puntos.

	Devuelve: Lista con los puntos agrupados a cada centroide.
	"""

	for i in range(0,np.shape(d)[0]):
		for j in range(0,np.shape(d)[1]):
			d[i,j] = math.sqrt((a[j,0] - m1[i,0])**2 + (a[j,1] - m1[i,1])**2)
	print('Distancias:\n' + str(d) + '\n')

	for x in range(0,np.shape(d)[1]):
		if d[0,x] < d[1,x]:
			g[0].append([a[x,0],a[x,1]])
		else:
			g[1].append([a[x,0],a[x,1]])
	return g


if __name__ == '__main__':
	kmedia()