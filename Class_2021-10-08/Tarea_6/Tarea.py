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

 