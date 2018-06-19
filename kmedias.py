#!/usr/bin/env python3
# -*- coding: utf-8 *-*

"""
Programa de agrupamiento K-medias.
"""

import math
import numpy as np

def kmedia(puntos,medias):
	"""Algoritmo de agrupamiento k-medias.

	Agrupa los puntos dependiendo del centroide mas cercano.
	Datos:	puntos = matriz de puntos.
			medias = matriz de medias (centroides).

	Tanto <m2> como <gn> se utilizan para el recalculo de medias y
	la nueva lista de grupos de puntos.
	"""
	
	medias_new = np.zeros((np.shape(medias)[0],np.shape(medias)[1]), dtype=float)
	gruponew= [[],[]]
	numero = 1

	print('\n============= ITERACION: ' + str(numero) + ' =============\n')
	
	g = distancia(puntos,medias)

	while (np.array_equal(g,gruponew) != True):

		#Esta parte se tiene que arreglar para evitar codigo repetido.
		for c in g[0]:
			medias_new[0,0] = c[0] + medias_new[0,0]
			medias_new[0,1] = c[1] + medias_new[0,1]
		if (len(g[0]) >= 0):
			medias_new[0,0] = medias_new[0,0]/len(g[0])
			medias_new[0,1] = medias_new[0,1]/len(g[0])
		else:
			print("Error, division por cero")
			break

		for c in g[1]:
			medias_new[1,0] = c[0] + medias_new[1,0]
			medias_new[1,1] = c[1] + medias_new[1,1]
		if (len(g[1]) >= 0):
			medias_new[1,0] = medias_new[1,0]/len(g[1])
			medias_new[1,1] = medias_new[1,1]/len(g[1])
		else:
			print("Error, division por cero")
			break

		print('\nNuevas medias:\n' + str(medias_new))

		numero += 1
		print('\n============= ITERACION: ' + str(numero) + ' =============\n')
		gruponew = distancia(puntos,medias_new)

		if (np.array_equal(g,gruponew) != True):
			g = gruponew
			medias_new = np.empty((np.shape(medias)[0],np.shape(medias)[1]))
			gruponew = [[],[]]



def distancia(puntos,medias):
	"""Calcula la dist. y agrupa puntos a cada centroide.

	Recibe: puntos = matriz de puntos a agrupar.
			medias = matriz de las medias.

	Devuelve: Lista con los puntos agrupados a cada centroide.
	"""
	grupos = []
	dist = np.empty((np.shape(medias)[0],np.shape(puntos)[0]))

	for totales in medias:
		grupos.append([])

	for i in range(0,np.shape(dist)[0]):
		for j in range(0,np.shape(dist)[1]):
			if (np.array_equal(puntos[j],medias[i]) == True):
				dist[i,j] = 0
			else:
				dist[i,j] = math.sqrt((puntos[j,0] - medias[i,0])**2 + (puntos[j,1] - medias[i,1])**2)

	print('Distancias:\n' + str(dist) + '\n')

	for x in range(0,np.shape(dist)[1]):
		if dist[0,x] < dist[1,x]:
			grupos[0].append([puntos[x,0],puntos[x,1]])
		else:
			grupos[1].append([puntos[x,0],puntos[x,1]])

	print('Puntos pertenecientes a ' + str(medias[0]) + ':\n' + str(grupos[0]) + '\n')
	print('Puntos pertenecientes a ' + str(medias[1]) + ':\n' + str(grupos[1]))
	
	return grupos


if __name__ == '__main__':

	puntos = np.matrix('1,12.5;3,10.5;3,12.5;3,14.5;3,18;5,18;5,16;5,14.5;5,13;6,9;8,10;9,11;8.5,12;7,13.5;8,16;0.5,10.5')
	medias = np.matrix('3,14.5;9,11')

	#puntos = np.matrix('1,1;2,1;4,3;5,4')
	#medias = np.matrix('1,1;2,1')

	#puntos = np.matrix('8,10;3,10.5;7,13.5;5,18;5,13;6,9;9,11;3,18;8.5,12;8,16')
	#medias = np.matrix('8,10;5,13')

	kmedia(puntos,medias)

	print('\nFIN DEL ALGORITMO.')