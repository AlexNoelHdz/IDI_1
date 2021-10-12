#%% -*- coding: utf-8 -*-
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
 

Practicar con estas dos tablas
proxima semana -> Resolver tabla mas grande
recorrer grafos
Leer con Pandas
Convertirla en array numpy
Funcion de energia -> 
TCP lista de posiciones 0-n
Si desisdes que es ciclica sumar primero y ultimo
Inicialmente ruta 0,1,2,3,4,5,6,7
Heuristico es algo que no tiene corroboracion cientifica, pero la experiencia dice que es correcto. 

funcion que recibre lista de energia y devuelve distancia 
temperatura incial alta y debes ir bajando

obtener nueva configuracion cercana a la que ya tienes
El numero de combinaciones es n-1 / 2 porque el primero no importa y una buena ruta se encuentra identica al reves
Algoritmicamente muy rapidas porque sale mejor aproximarse que tardarse. 
Primer paso, tomar dos posiciones random de la lista e intercambiarlas 
Si salen repetidas no hay bronca porque es mejor que estar revisando contra las que ya salieron computacionalmente. 

Leer la matriz y guardar la distancia en un array
funcion de energia
def_energia(ruta) -> devuelve la energia total de la ruta sumando por pares i, i=1 
    return

Variable temperatura con valor alto inicial T, depende de cada problema.
x Lista del 0 al 7
while(T> final)
#K es montecarlo, variable, limitado al tiempo que tengas 10000
    for k veces
    Calcular energia x prima (intercambio de dos posiciones aleatorias) y energia x
    Primero copiar x en x prima y luego cambiarla 
    sacar diferencia
    calcular q np.ex
    P aleatorio con random entre 0 y 1
    if p < q
    x = x prima (con slising x[:] o .copy)
    bajas T con las formulas de la vez pasada, bajo una curva de concavidad positiva. Primero rapido y luego lento.
    Sacar el X (90) por ciento a la temperatura inicial es el mas facil
    
    Contador de ciclos para saber cuantas iteraciones metiste
Links:
    [Medir tiempo] - https://ellibrodepython.com/tiempo-ejecucion-python
"""
"""Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

"""
"""
import time
#How to use time
inicio = time.time()
#Stuff
fin = time.time()
print(fin-inicio) # 1.5099220275878906
"""
#%%
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

current_sheet_name, k, T_i, T_f = '8c_short', 60, 1, 0 
solution , distancia, interacciones = simulated_annealing(current_sheet_name, k, T_i, T_f) 
print(f"La mejor ruta es {solution} con una distancia de {distancia} y {interacciones} interacciones.")
print(f"sheet: {current_sheet_name}, k: {k}, T_i: {T_i}, T_f: {T_f}")

current_sheet_name, k, T_i, T_f = '15c_short', 60, 10, 0 
solution , distancia, interacciones = simulated_annealing(current_sheet_name, k, T_i, T_f) 
print(f"La mejor ruta es {solution} con una distancia de {distancia} y {interacciones} interacciones.")
print(f"sheet: {current_sheet_name}, k: {k}, T_i: {T_i}, T_f: {T_f}")


