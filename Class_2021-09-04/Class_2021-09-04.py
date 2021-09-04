# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 08:16:05 2021

@author: Alejandro Hernandez
Numerical python
Cada librería tiene su tipo de datos
Con numpy los objetos son
Las listas se utilizan en su mayoría
Cuando vas a usar datos sin hacer operaciones
Los arreglos de numpy tienen las propiedades de una lista
más adiciones
"""
import numpy as np 

#declarar lista por extension:
#La lista es un conjunto no ordenado de objetos
M=[3,4,5,'hola',3.4,1]
#Las listas son indexables e iterables
x = M[3]

"""
slicing
pedir un subconjunto de la lista basado en criterios
"""
#Internamente hace ciclo for
#comienzo en 2 y al llegar al 5 salgo
#non exclusive end
x = M[2 : 5 ] 
#steps since x =  1 to x < 5 steps 3 
x = M[1 : 5 : 3] 
x = M[1 : 5 : -1] 
#el slicing tiene defaults
x = M[::]
#Se puede voltear la cadena
x = M[::-1]

#Numpy array
#El arreglo es un arreglo de enteros
#Los enteros son int32 (32 bits)
#Tamaño acotado: dtype = 'int8'
#Por ejemplo, el 357 lo acota a 8 bits (101 entero)
L= [1,2,3]
L.append(357)
L.append(255)
A = np.array(L, dtype = 'int8')
#unsigned
L.append(255)
B = np.array(L, dtype = 'uint8')
f = 1.8
g = 4
h = f + g #float mata int

h = g + True  #booleano se interpreta como 1 o 0

"""
3 maneras de crear listas
Extension / Comprensión

Comprensión: Si la lista tiene una lógica la ordena
"""
#Arrange permite algo como el slicing generado
#Convertir
B = list(np.arange(4, 100, 3))

#Otra manera de generar lista por comprensión
#For inline
s = [i**2 for i in range(20)]
A_array = np.array(L)
B_array = np.array(B)
s_arrange = np.array(s)
A_array = np.arange(50, 54)
B_array = np.arange(1, 5)

#sumar dos arreglos
C = A_array+B_array
C = sum(A_array<50)

#2Se puede indexar por booleanos
C=B_array[A_array<50]

S = np.array([i**2 for i in range(20)])
#extraer multiplos de 3
C = S%3
C = S[S%3==0]


L= [1,2,300,400]
A = np.array(L)
#Ordenar por Columns (Fortran)
D = np.reshape(A, (2,2),'F')
#Ordenar por Rows (languaje C)
D1 = np.reshape(A, (2,2),'C')
Y = sum(D)
Y = np.sum(D, 0, 'uint8')

W = np.zeros((3,9), 'int')

S = np.array([i**2 for i in range(20)])
#where es buena idea
X = S[np.logical_and(S<30, S%2==0)]

P = np.all(S>100)

Q = np.where(S<100,S,0)
#discriminar
R = S[S<100]*3







