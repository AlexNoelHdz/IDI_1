# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:30:38 2021

@author: anhernan
"""

import numpy as np

#Genere código en Python que, usando N=1000 valores aleatorios y 
N = 1000

np.random.seed(100)
#mediante el teorema integral del valor medio, 

#estime el valor de LaTeX: \int_1^4\frac{1}{x^2+4}dx

x = np.random.uniform(1,4,N)

y = np.mean(1/(x**2+4))*(4-1)


#Ahora genere una lista con 100 aproximaciones (N=1000 en cada una) 
#y calcule la media y la desviación estándar de dicha lista.

L = []
for _ in range(100):
    x = np.random.uniform(1,4,N)
    y = np.mean(1/(x**2+4))*(4-1)
    L.append(y)


mean = np.mean(L)

std = np.std(L)



#Imprima el error absoluto entre el resultado correcto de la integral
# y la media calculada.

absolute_value = 0.32175 # https://www.integral-calculator.com/

print("Error is %.5f"%(absolute_value-mean))