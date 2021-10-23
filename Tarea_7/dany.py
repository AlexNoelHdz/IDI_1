# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 00:01:33 2021

@author: anhernan
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

c54 = np.array(pd.read_excel('SA2.xlsx', sheet_name='54c_test',index_col=0))

def nueva_configuracion(conf):
    conf2 = conf.copy()
    i, j = np.random.randint(0, len(conf) - 1, 2)
    # i, j = np.random.randint(1, len(conf) - 2, 2) # No cambiar ciudad inicial ni final.
    conf2[i], conf2[j] = conf2[j], conf2[i]
    return conf2.copy()

# Para graficar las energías
def see_annealing(costos):
    plt.figure()
    plt.title("Evolución de las configuraciones y los costos.")
    plt.plot(costos, 'b')
    plt.xlabel('Costos')
    plt.show()
    
# Función de energia que hace calculo con la configuración (Ej: Suma total de la distancia.)
def energia(x, TD):
    # x: configuración.
    # TD: tabla de distnacias.
    # distancias = list(TD[x[i-1]][x[i]] for i in range(len(x)))
    distancias = list(TD[x[i-1]][x[i]] for i in range(len(x)-1)) # No cíclica.
    return np.sum(distancias)

# Funciones para bajar la temperatura.
def temperatura(T_0, t, tipo_funcion, T_f, k):
    if tipo_funcion == "logaritmo":
        res = T_0/np.log(t + 1)
    elif tipo_funcion == "porcentaje":
        res = T_0*(0.85**t)
    elif tipo_funcion == "aprensivos":
        res = T_0*(T_f/T_0)**(t/k)
    return res

# Función de recocido simulado.
def Annealing(T_0, k, x, T_f, TD, tipo_funcion): 
    # T_0: temperatura inical.
    # k: número de veces a calcular.
    # x: es el listado de configuraciones.
    # T_f: temperatura final.
    # TD: tabla de distancias.
    T = T_0 # Temperatura Inicial.
    t = 1 # iteraciones
    costos = []
    while T > T_f:
        for _ in range(k):
            x2 = nueva_configuracion(x) # x2 = x'
            dif_E = energia(x2, TD) - energia(x, TD) # Error
            # dif_E = -(energia(x2, TD) - energia(x, TD)) # Para maximizar.
            q = np.exp(-dif_E/T) # Probabilidad de rechazo.
            p = np.random.random() # Probabilidad de tolerancia.
            
            if dif_E < 0:
                x = x2.copy() # Tomamos la nueva configuración al ser menor
            elif p < q:
                x = x2.copy() # Tomamos la nueva configuración aún siendo peor
        costos.append(energia(x, TD))
        T = temperatura(T_0, t, tipo_funcion, T_f, k)
        t = t + 1
    return costos, x.copy(), t*k # Configuración óptima.

#%% Nunca pasar de 1'000,000 de rutas revisadas.
T_01 = 75
k1 = 900
TD1 = c54
T_f1 = 0.7
tipo_funcion1 = "aprensivos"

costos, conf1, iter1 = Annealing(T_01, k1, np.arange(len(TD1)), T_f1, TD1, tipo_funcion1)

print(energia(conf1, TD1), conf1)
print(f' Número de iteracciones: {iter1}')
see_annealing(costos)

#%% Cambiando la función para decrementar la temperatura.
T_01 = 7.5
k1 = 2300
TD1 = c54
T_f1 = 0.17*T_01
tipo_funcion1 = "logaritmo"

costos, conf1, iter1 = Annealing(T_01, k1, np.arange(len(TD1)), T_f1, TD1, tipo_funcion1)

print(energia(conf1, TD1), conf1)
print(f' Número de iteracciones: {iter1}')
see_annealing(costos)

#%% Fijando la primer ciudad como Copenhagen y la final como Lynge.
T_01 = 75
k1 = 900
TD1 = c54
T_f1 = 0.7
tipo_funcion1 = "aprensivos"
x1 = np.arange(len(TD1))
x1[0], x1[-1] = x1[6], x1[33]

costos, conf1, iter1 = Annealing(T_01, k1, x1, T_f1, TD1, tipo_funcion1)

print(energia(conf1, TD1), conf1)
print(f' Número de iteracciones: {iter1}')
see_annealing(costos)