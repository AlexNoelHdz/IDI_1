# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernandez
Genere código en Python que, usando N=1000 valores aleatorios y mediante el teorema integral del valor medio, estime el valor de ∫1 to 4 (1/ (x^2 + 4)) dx

Ahora genere una lista con 100 aproximaciones (N=1000 en cada una) y calcule la media y la desviación estándar de dicha lista.
N puntos correr 100 veces
Imprima el error absoluto entre el resultado correcto de la integral y la media calculada.
"""
#integral exacta .32
import numpy as np
np.random.seed(100)
N = 1000
A = 1
B = 4
X = np.random.uniform(1,4,N)
I = (B-A) * np.mean((1/(X**2+4)))

aproximaciones = []
for _ in range(100):
    X = np.random.uniform(1,4,N)
    I = (B-A) * np.mean((1/(X**2+4)))
    aproximaciones.append(I)

media = np.mean(aproximaciones)
desv_estandar = np.std(aproximaciones)
print("Media: {} \n Desviación estandar: {}".format(media, desv_estandar))

#https://www.wolframalpha.com/input/?i=int+from+1+to+4++1+%2F+%28x%5E2+%2B4%29
valor_real = 0.32175
print("El error absoluto es: {}".format(abs(media - valor_real)))