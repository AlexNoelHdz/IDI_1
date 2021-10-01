# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernandez
"""
import numpy as np
import numpy.random as rd
np.random.seed(666)
# 1. Genere una matriz Q de 5x5 con elementos aleatorios reales en [1,10)
Q = rd.uniform(1,10,(5,5))
# 2. Imprima el porcentaje de elementos de la matriz Q que están por encima del promedio.
print(f"Porcentaje de elementos de Q encima del promedio: { (Q > Q.mean()).sum() * (100 / sum(len(row) for row in Q)) }")
# 3. Genere una lista L con 15 listas de 100 números reales en [0,8)
R = [rd.uniform(0, 8, 100) for i in range(15)]
# 4.Genere una lista M con los promedios de cada una de las 15 listas de L, 
M = [r.mean() for r in R]
# luego imprima el promedio de los promedios. 
print(f"Promedio de los promedios de M: {np.mean(M)}")
# 5. Emule el experimento de obtener la suma de dos dados 
suma_dados =  rd.choice([1,2,3,4,5,6],2).sum()
# y genere una lista aleatoria D con los resultados de 1000 lanzamientos 
# (note que no todos los resultados son igual de probables).
D = [rd.choice([1,2,3,4,5,6], 2).sum() for i in range(1001)]
# 6. Suponga que tiene una caja con dos canicas rojas, tres azules y 5 blancas. 
canicas = ['r', 'r', 'a','a','b','b','b','b','b']
# Quiere emular el proceso de sacar 3 canicas de la caja 
# de forma que no se regresa la canica que ya se sacó. 
tres_canicas = rd.choice(canicas, 3, replace=False)
# Cree una lista C con los resultados de 10 experimentos (es decir, una lista de 10 listas con 3 elementos). 
C = [rd.choice(canicas, 3, replace=False) for i in range(10)]