# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 08:14:29 2021

@author: Alejandro Hernandez
Desarrollar código en Python que:

Inicialice la semilla de aleatoriedad con un valor fijo arbitrario
Genere una lista G con los elementos {3,6,9,...,39}
Imprima una permutación aleatoria de los elementos de G.
Obtenga una lista H con 4 elementos de G seleccionados de forma aleatoria (sin reemplazo).
Genere un arreglo L de 100 números aleatorios enteros en [5,100]
Imprima la cantidad de números pares en L.
Genere una lista M de 100 números aleatorios reales en [3,10)
Imprima la suma de los elementos de M
Genere una lista R con 20 listas de 50 números reales en [0,10)
Cada uno de los incisos debe resolverse con una sola línea de código.
#Contar booleanos
# pares = L%2==0
"""
import numpy as np
# Inicialice la semilla de aleatoriedad con un valor fijo arbitrario
np.random.seed(666)
# Genere una lista G con los elementos {3,6,9,...,39}
G = np.arange(3,41,3)
# Imprima una permutación aleatoria de los elementos de G.
np.random.shuffle(G)
print("{}".format(G))
# Obtenga una lista H con 4 elementos de G seleccionados de forma aleatoria (sin reemplazo).
H = np.random.choice(G, 4,False)
# Genere un arreglo L de 100 números aleatorios enteros en [5,100]
L = np.random.randint(5,100,(100))
# Imprima la cantidad de números pares en L. 
print(sum(L%2==0))
# Genere una lista M de 100 números aleatorios reales en [3,10)
M = np.random.uniform(3,10,100)
# Imprima la suma de los elementos de M
print(sum(M))
# Genere una lista R con 20 listas de 50 números reales en [0,10)
R = list(list(np.random.uniform(0, 10, 50)) for i in range(20))