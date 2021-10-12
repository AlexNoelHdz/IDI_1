# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernandez

Método Simulated Annealing
Link: https://machinelearningmastery.com/simulated-annealing-from-scratch-in-python/

Simulated Annealing: Intenta resolver problemas que están basados en un espacio de configuración.

Función de energía: Es una función matemática que puede tomar una configuración y devolver un valor. 
Este algorítmo surgió de una idea termodinámica.
El objetivo es encontrar la configuración que tenga más o menos energía.
Se puede visualizar como un problema de optimización (encontrar el máximo y mínimo de una función)
Código corto: revisa la energía de cada una de las configuraciones y dame la que tiene más. 

Un espacio de configuraciones es un espacio discreto (Hay n configuraciones y son muy claras), osea que es distinto
a una función continua en cálculo.

Problema a resolver: Travelling Salesman Problem (Problema del agente de ventas.)
Este problema es un pretexto para entender el porqué este tipo de problemas llegó a la computación y luego hasta
la inteligencia artificial. 
Se visualizan nodos con las conexiones entre ciudades de francia. 
Supon que un agente de ventas distribuye pedidos y recorrerá todas las ciudades 
¿Cómo hacer el recorrido de manera que optimice los recursos?
El cómo depende de la función de energía. 
Las configuraciones son cada posible manera en la que puedo hacer el recorrido. 
La función de energía toma cada manera de hacerlo y devuelve un valor numérico para determinar
cuál es mejor dependiendo las variables. 
Puedes optimizar tiempo, distancia, gasto de gasolina etc y generar diferentes funciones de energía. 

-> De cualquier punto puedes llegar a cualquier punto
 

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
        T = T / float(i + 1)
        t += 1
    return x.copy() , energia(x, data), t*k

# current_sheet_name, k, T_i, T_f = '8c_short', 60, 1, 0 
# solution , distancia, interacciones = simulated_annealing(current_sheet_name, k, T_i, T_f) 
# print(f"La mejor ruta es {solution} con una distancia de {distancia} y {interacciones} interacciones.")
# print(f"sheet: {current_sheet_name}, k: {k}, T_i: {T_i}, T_f: {T_f}")

current_sheet_name, k, T_i, T_f = '15c_short', 100, 10, 0 
solution , distancia, interacciones = simulated_annealing(current_sheet_name, k, T_i, T_f) 
print(f"La mejor ruta es {solution} con una distancia de {distancia} y {interacciones} interacciones.")
print(f"sheet: {current_sheet_name}, k: {k}, T_i: {T_i}, T_f: {T_f}")
