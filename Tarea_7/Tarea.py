# -*- coding: utf-8 -*-
"""
"""
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def energia(x, data, ciclica):
    """Obtiene el costo o distancia de la configuración actual de energía
    """
    total = 0
    if(ciclica):
        for i in range(0,len(x)):
                total += data[x[i-1]][x[i]] 
    else:
        for i in range(0,len(x)-1):
               total += data[x[i]][x[i+1]] 
    return total

def intercambio(x):
    stop = len(x) - 1
    i , j = np.random.randint(0, stop, 2) 
    # i , j = np.random.choice(range(0,stop), 2, False)    
    x_1 =  x.copy() 
    x_1[i], x_1[j] = x_1[j], x_1[i] 
    return x_1

def intercambio_fijo(x):
    """
    Tipo de intercambio que respeta el inicio y final de la ruta
    """
    stop = len(x) - 2
    i , j = np.random.randint(1, stop, 2) 
    # i , j = np.random.choice(range(1,stop), 2, False)    
    x_1 =  x.copy() 
    x_1[i], x_1[j] = x_1[j], x_1[i] 
    return x_1

def Get_temperature_1(T_i, t):
    return T_i / float(t + 1)

def simulated_annealing(x, ciclica, ruta_fija, ciclo_minimo, temp_function, k, T_i, T_f):
    """
    Solve problem by Simulated Annealing Algorithm
    Parameters
    ----------
    ciclica : TYPE
        Determina si se tiene que regresar al origen.
    ruta_fija : TYPE
        Determina si el comienzo y fin son fijos.
    ciclo_minimo : TYPE
        Determina si se desea obtener el ciclo mínimo o máximo.
        
    k : TYPE
        Cantidad de veces que se ajusta y revisa la ruta en una iteración.
    T_i : TYPE
        Temperatura inicial.
    T_f : TYPE
        Temperatura Final.
    """
    T = T_i
    t = 0 
    #Variables Globales
   
    while(T > T_f):
        for i in range(k):
            if(ruta_fija):
                x1 = intercambio_fijo(x)
            else:
                x1 = intercambio(x)
            delta_E = energia(x1, data, ciclica) - energia(x, data, ciclica)
            q = np.exp(-delta_E / T)
            if ciclo_minimo:
                if np.random.rand() < q:
                    x = x1.copy()
            else:
                if np.random.rand() > q:
                    x = x1.copy()
        t += 1
        T = temp_function(T_i,t)
    return x.copy() , energia(x, data, ciclica), t*k

def Simulate(x, current_sheet_name, ciclica, ruta_fija, ciclo_minimo, temp_function, k, T_i, T_f, run_times):
    results = []
    for _ in range(run_times):
        print("----------------------------------------------------------------------------------")
        solution , distancia, interacciones = simulated_annealing(x, ciclica, ruta_fija, ciclo_minimo,temp_function, k, T_i, T_f) 
        print(f"sheet: {current_sheet_name}, k: {k}, T_i: {T_i}, T_f: {T_f} -> ")
        print(f"La mejor ruta es {solution} con una distancia de {distancia} y {interacciones} interacciones.")
        results.append(solution)
    if(run_times>1):   
        print(f"Desviacion Estandar: {np.std(results)}")
    

#%%Encuentre el ciclo de valor mínimo. Decida la manera de decrementar la temperatura para
# obtener la mejor respuesta que le sea posible.
# La mejor ruta es [42 33 31  2 44  9 51  1 34 43 15 45 50 10 46 28 49  0 17 38 26 12  6  5
#  48  7 39 35 52  4 30 47 27  3 37 11 36 24  8 21 19 23 16 18 20 22 41 14
#  32 25 29 40 13 53] con una distancia de 496.2155187100001 y 999000 interacciones.
current_sheet_name, ciclica, ruta_fija, ciclo_minimo, k, T_i, T_f, run_times = '54c_test', True, False, True,  1000, 900, .9, 1
data = np.array(pd.read_excel('SA2.xlsx', sheet_name=current_sheet_name,index_col=0))
x = np.array(range(0,len(data[0])))
Simulate(x,current_sheet_name, ciclica, ruta_fija, ciclo_minimo, Get_temperature_1, k, T_i, T_f, run_times)

# %%Ahora utilice una forma distinta para disminuir la temperatura (con respecto a la usada en
# el inciso anterior). ¿Qué modificación requirió hacer para llegar a la respuesta obtenida
# antes?
# La mejor ruta es [40 13 29 22  8 24 21 19 23 16 18 20 32 25 14 41  3 30  4 47 27 11 37 36
#  31  2 44  9 51 45 42 15 33 43 34  1  6  7 39 52 35 48  5 12 26 38 17  0
#  49 28 46 10 50 53] con una distancia de 559.6182494 y 20000 interacciones.
#La k se vuelve mucho más importante y controlas con mayor precisión el comportamiento
#Para obtener una respuesta satisfactoria se usó una k proporcional a la temperatura inicial, pero suficientemente grande

current_sheet_name, ciclica, ruta_fija, ciclo_minimo, k, T_i, T_f, run_times = '54c_test', True, False, True,  20000, 2, 1, 1
data = np.array(pd.read_excel('SA2.xlsx', sheet_name=current_sheet_name,index_col=0))
x = np.array(range(0,len(data[0])))
def Get_temperature_controladores(T_i, t):
    return T_i * (float(T_f/T_i)**t/k)
Simulate(x,current_sheet_name, ciclica, ruta_fija, ciclo_minimo, Get_temperature_controladores, k, T_i, T_f, run_times)

# %%Modifique su código para encontrar el ciclo de valor máximo. De nuevo, decida la manera
# de decrementar la temperatura para obtener la mejor respuesta que le sea posible.
# La mejor ruta es [30 22 48 32  6 40 19 43 11  9 35 20 49 25 44 52  3 17 18  5 13  4 33  0
#   2 15 26 42 27 50 47 45 24  1  8 10 31 28 37 46 23 34 36  7 16 38 41 39
#  14 12 29 51 21 53] con una distancia de 2267.04110472 y 899000 interacciones.
current_sheet_name, ciclica, ruta_fija, ciclo_minimo, k, T_i, T_f, run_times = '54c_test', True, False, False,  1000, 900, 1, 1
data = np.array(pd.read_excel('SA2.xlsx', sheet_name=current_sheet_name,index_col=0))
x = np.array(range(0,len(data[0])))
Simulate(x,current_sheet_name, ciclica, ruta_fija, ciclo_minimo, Get_temperature_1, k, T_i, T_f, run_times)

# %% Ahora suponga que la ruta no debe ser cíclica. Encuentre la ruta de valor mínimo sin
# importar el punto de inicio y el de final.
# La mejor ruta es [35 52 39  7 48  5 12  6 26 38 17  0 49 28 46 10 15 33 22 37 11 36 24  8
#  21 19 23 16 18 20 32 25 14 41 13 29 40 45 50 34 43  1 51  9 44  2  4 30
#  47 27  3 31 42 53] con una distancia de 377.33749579000005 y 1198800 interacciones.
current_sheet_name, ciclica, ruta_fija, ciclo_minimo, k, T_i, T_f, run_times = '54c_test', False, False, True,  1200, 800, .8, 1
data = np.array(pd.read_excel('SA2.xlsx', sheet_name=current_sheet_name,index_col=0))
x = np.array(range(0,len(data[0])))
Simulate(x,current_sheet_name, ciclica, ruta_fija, ciclo_minimo, Get_temperature_1, k, T_i, T_f, run_times)


# %% Por último, suponga que se fija como lugar de inicio Copenhagen y como destino final Lynge.
# Encuentre la mejor ruta de valor mínimo para este caso.
# La mejor ruta es [ 6 26 38 12  6  5  4 30 51  9 44  2 47 27 36 24  8 21 19 23 16 18 20 11
#  37 22 31  3 33 15 34  1 43 50 45 42 13 41 14 32 25 29 40 10 46 28 49 17
#  48  7 39 35 52 33] con una distancia de 550.7599986799999 y 899000 interacciones.
current_sheet_name, ciclica, ruta_fija, ciclo_minimo, k, T_i, T_f, run_times = '54c_test', True, True, True,  1000, 900, 1, 1
data = np.array(pd.read_excel('SA2.xlsx', sheet_name=current_sheet_name,index_col=0))
x = np.array(range(0,len(data[0])))
x[0], x[-1] = x[6], x[33]
Simulate(x,current_sheet_name, ciclica, ruta_fija, ciclo_minimo, Get_temperature_1, k, T_i, T_f, run_times)