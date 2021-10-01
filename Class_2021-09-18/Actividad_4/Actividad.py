# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernandez

Usando Python:

Genere una lista L con los resultados de emular 1000 veces el experimento de obtener la suma de dos dados. Suponga que los dados están cargados y el 5 tiene el doble de probabilidades que los demás. ¿Qué porcentaje de los resultados fue 10?
Genere una lista M con los resultados de emular las respuestas aleatorias de 1000 exámenes de 8 preguntas verdadero-falso.  ¿Cuál fue el promedio de calificación sobre 100?
Se sabe que por un crucero pasan en promedio 20 coches por minuto. Emule aleatoriamente los resultados de tomar mediciones cada minuto durante una hora. ¿Cuál fue el mayor y el menor valor obtenido?
El coeficiente intelectual (IQ) es un estimador de la inteligencia general. Se distribuye normalmente con una media de 100 y desviación estándar de 15.  Genere una lista Q que emule los IQ de una muestra aleatoria de 500 personas. Si se considera a una persona superdotada si su IQ es igual o mayor a 130, ¿cuántos superdotados se obtuvieron en la simulación?
"""
import numpy as np
np.random.seed(666)
# 1.-Genere una lista L con los resultados de emular 1000 veces el experimento de obtener la suma de dos dados. 
# Suponga que los dados están cargados y el 5 (número) tiene el doble de probabilidades que los demás.
#Separarlo en arreglo y lista para terminarlo
#no está prohibido usar cosas de antes
#No binomial. Random, choice etc
L = [np.random.choice([1,2,3,4,5,6], 2,p=[1/7,1/7,1/7,1/7,2/7,1/7]).sum() for i in range(1000)]
# ¿Qué porcentaje de los resultados fue 10?
L_array = np.array(L)
print(f"Porcentaje de elementos de L igual a 10: { (L_array == 10).sum() * (100 / (L_array == L_array).sum()) }")
# 2.- Genere una lista M con los resultados de emular las respuestas aleatorias de 1000 exámenes de 8 preguntas verdadero-falso
M = list(np.random.binomial(8, 1/2, 1000))
#¿Cuál fue el promedio de calificación sobre 100?
promedio_sobre_100 = (np.array(M) * (100/8)).mean()
print(f"Promedio sobre 100 de 100 examenes de 8 preguntas: {promedio_sobre_100}")
# 3.- Se sabe que por un crucero pasan en promedio 20 coches por minuto. 
#Emule aleatoriamente los resultados de tomar mediciones cada minuto durante una hora.
Coches_por_hora = list(np.random.poisson(20,60))
#¿Cuál fue el mayor y el menor valor obtenido?
min_coches_por_hora = min(Coches_por_hora)
max_coches_por_hora = max(Coches_por_hora)
# 4.- El coeficiente intelectual (IQ) es un estimador de la inteligencia general. 
# Se distribuye normalmente con una media de 100 y desviación estándar de 15.  
# Genere una lista Q que emule los IQ de una muestra aleatoria de 500 personas. 
IQ_500_Personas = list(np.random.normal(100, 15,500))
# Si se considera a una persona superdotada si su IQ es igual o mayor a 130, 
# ¿cuántos superdotados se obtuvieron en la simulación?
print(f"Personas super dotadas entre 500: {(np.array(IQ_500_Personas) > 130).sum()}")