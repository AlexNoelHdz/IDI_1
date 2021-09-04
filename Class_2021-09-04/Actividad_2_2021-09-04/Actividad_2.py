# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:08:41 2021

@author: Alejandro Hernandez

Desarrollar código en Python que:

1. genere la matriz A=(3 7 5 11)y la matriz B=(−2 9 4 10)
2. calcule la matriz C=3A+B−I2, donde I2es la matriz identidad de 2×2
3. una las matrices A y B de forma que se obtenga la matriz D=(3 7 5 11 −2 9 4 10)
4. imprima la suma de los elementos de D  y la cantidad de números pares que tiene
5. genere una matriz F  de 10 x 10 que contenga los números naturales del 1 al 100 colocados por columna
6. imprima la suma de los valores de F cuyos valores estén en el intervalo [10,20]

"""
import numpy as np
#===1===#
A = np.reshape([3, 7, 5, 11], (2,2),'F')
B = np.reshape([-2, 9, 4, 10], (2,2),'F')
#===2===#
I2 = np.identity(2)
C = np.multiply(3, A) + B - I2
#===3===#
D = np.concatenate((A, B), axis=1)
#===4===#
print(f'Suma de D: {np.sum(D)}')
print(f'Suma de pares de D: {len(D[np.where(D%2 == 0)])}')
#===5===#
F = np.arange(1,101).reshape(10,10, order = 'F')
#===6===#
print(f'Valores de F n el intervalo [10,20]: {F[np.logical_and(F>=10, F<=20)].sum()}')
