# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernandez

Realice código en Python para implementar el algoritmo Simulated Annealing  
para resolver un problema de TSP (https://en.wikipedia.org/wiki/Travelling_salesman_problem). 
Es decir, dadas N ubicaciones y su matriz de distancias, encontrar una ruta cíclica óptima (de menor distancia) entre ellas.

Puede realizar pruebas con las siguientes matrices de distancias (En la ruta del código)

Adjunte sólo el código.

"""

import pandas as pd
import numpy as np

def energia(x, data):
    """Obtiene el costo o distancia de la configuración actual de energía
    """
    total = 0
    for i in range(0,len(x)):
        total += data[x[i-1]][x[i]] 
    return total

def intercambio(x):
    stop = len(x) - 1
    i , j = np.random.randint(0, stop, 2) 
    # i , j = np.random.choice(range(0,stop), 2, False)    
    x_1 =  x.copy() 
    x_1[i], x_1[j] = x_1[j], x_1[i] 
    return x_1

def simulated_annealing(current_sheet_name, k, T_i, T_f):
    T = T_i
    t = 0 
    #Variables Globales
    data = np.array(pd.read_excel('data.xlsx', sheet_name=current_sheet_name))
    x = np.array(range(0,len(data[0])))
    while(T > T_f):
        for i in range(k):
            x1 = intercambio(x)
            delta_E = energia(x1, data) - energia(x, data)
            q = np.exp(-delta_E / T)
            if np.random.rand() < q:
                x = x1.copy()
        t += 1
        T = T_i / float(t + 1)
    return x.copy() , energia(x, data), t*k

print("----------------------------------------------------------------------------------")
current_sheet_name, k, T_i, T_f = '8c_short', 30, 10, 1 
solution , distancia, interacciones = simulated_annealing(current_sheet_name, k, T_i, T_f) 
print(f"sheet: {current_sheet_name}, k: {k}, T_i: {T_i}, T_f: {T_f} -> ")
print(f"La mejor ruta es {solution} con una distancia de {distancia} y {interacciones} interacciones.")

print("------------------------------------------------------------------------------------")
current_sheet_name, k, T_i, T_f = '15c_short', 5000, 10, 1
solution , distancia, interacciones = simulated_annealing(current_sheet_name, k, T_i, T_f) 
print(f"sheet: {current_sheet_name}, k: {k}, T_i: {T_i}, T_f: {T_f} -> ")
print(f"La mejor ruta es {solution} con una distancia de {distancia} y {interacciones} interacciones.")
