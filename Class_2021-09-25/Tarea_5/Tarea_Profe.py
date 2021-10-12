# -*- coding: utf-8 -*-
"""
@author: 

Utilice el método de Montecarlo para obtener la probabilidad estimada de triunfo 
para el juego "Aguja de Buffon". 
Llame L a la longitud de la aguja y D a la distancia entre las líneas. 
Muestre con Montercarlo que si L = D la probabilidad es P ≈ igual a 2/π

¿Qué valor obtiene si la aguja mide la mitad de la separación entre líneas?

¿Es posible estimar el valor de π con este juego? Explique.

Use N = 100000 experimentos.

Adjunte su código con las respuestas como comentario en el archivo py.    

Hola a tod@s.

Les dejo una posibilidad de solución de la tarea 5 para D=L=1

import numpy as np

N = 1000000
D,L = 1,1

x = np.random.uniform(0,D,N)
t = np.random.uniform(0,np.pi/2,N)
probabilidad = sum(x+L*np.sin(t)>D)/N
aprox_de_pi= 2/probabilidad

La idea es que vean que no se necesitan ciclos si se aprovecha el size de las funciones en numpy.

Cualquier duda, me comentan.

Saludos y buen fin de semana.
"""

