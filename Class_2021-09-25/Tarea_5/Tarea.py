# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernandez
Utilice el método de Montecarlo para obtener la probabilidad estimada de triunfo 
para el juego "Aguja de Buffon". 
Llame L a la longitud de la aguja y D a la distancia entre las líneas. 
Muestre con Montercarlo que si L = D la probabilidad es P ≈ igual a 2/π

¿Qué valor obtiene si la aguja mide la mitad de la separación entre líneas?

¿Es posible estimar el valor de π con este juego? Explique.

Use N = 100000 experimentos.

Adjunte su código con las respuestas como comentario en el archivo py.  
"""

import numpy as np

N = 1000000
#Llame L a la longitud de la aguja y D a la distancia entre las líneas. 
D,L = 666,666
#%% Muestre con Montercarlo que si L = D la probabilidad es P ≈ igual a 2/π
x = np.random.uniform(0,D,N) #Aleatorio de distancia
t = np.random.uniform(0,np.pi/2,N) #Aleatorio del ángulo
prob = sum(x+L*np.sin(t)>D)/N#Porcentaje de agujas que cruzaron
print("La probabilidad [{}] es aproximadamente igual a [{}]".format(prob, (2/np.pi)))
#%% ¿Qué valor obtiene si la aguja mide la mitad de la separación entre líneas?
#Llame L a la longitud de la aguja y D a la distancia entre las líneas. 
D,L = 333,666
x = np.random.uniform(0,D,N)
t = np.random.uniform(0,np.pi/2,N)
prob = sum(x+L*np.sin(t)>D)/N 
print("El valor obtenido si la aguja mide la mitad de la separación entre lineas es: [{}]".format(prob))
#%%¿Es posible estimar el valor de π con este juego? Explique.
"""
Si, es posible. Volviendo a los valores iniciales y partiendo de que la probabilidad  es P ≈ igual a 2/π
Despejando  es π ≈ 2/P
"""
D,L = 666,666
x = np.random.uniform(0,D,N)
t = np.random.uniform(0,np.pi/2,N)
prob = sum(x+L*np.sin(t)>D)/N
print("El valor de Pi es aproximadamente: {}".format(2/prob))

cae_o_no = x+L*np.sin(t)>D 