# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:55:55 2021

@author: ASBHBHAT
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

np.random.seed(10)

#En el juego Calabozos y dragones se usan dados no cúbicos.
#Suponga que tiene dados en forma de octaedro cuyas caras marcan 1,2,2,3,4,6,10,12. 
#Emule el experimento de obtener la suma de dos de esos dados
#genere una lista aleatoria L con los resultados de 1000 lanzamientos.
#Imprima el resultado que más se obtuvo en el experimento y el que menos.

dice = [1, 2, 2, 3, 4, 6, 10, 12]

L = [np.random.choice(dice) + np.random.choice(dice) for x in range(1000)]

#y, x, shape_bin = plt.hist(L)

Max = [k for k,v in  Counter(L).items() if v == max(v for k,v in Counter(L).items() if v>1)][0]
Min = [k for k,v in  Counter(L).items() if v == min(v for k,v in Counter(L).items() if v>1)][0]

#print(int(x[np.where(y == y.max())]))
#print(int(x[np.where(y == y.min())]))

print(Max)
print(Min)
#Suponga que tiene una baraja que tiene las cartas numeradas del 1 al 10 de cuatro colores distintos 
#(azul, rojo, verde y amarillo), es decir, 40 cartas en total. 
#Emule el proceso de repartir 5 cartas a un jugador. 
#Repita el proceso 5000 veces e imprima según este experimento, 
#¿qué tan probable es obtener un juego que sume más de 30 puntos?

green_cards = yellow_cards = red_cards = blue_cards = np.arange(1, 11)
cards = np.concatenate((blue_cards, yellow_cards, red_cards, green_cards))
np.random.shuffle(cards)

experiment = [np.random.choice(cards, size=5, replace=False).sum() for i in range(5000)]

pron_gt_30 = len([x for x in experiment if x > 30])/len(experiment)

#Emule el evento de contestar un examen de 12 preguntas,
#cada una de 4 opciones (sólo una correcta).
#Entregue una lista M con las calificaciones (sobre 100) de 500 exámenes contestados aleatoriamente.

M = list(np.random.binomial(12, 0.25, 500)*100/12)

#Se sabe que durante un turno de una fábrica se producen 10 pelotas 
#cada minuto en promedio. 
#Emule aleatoriamente los resultados de tomar mediciones
#cada minuto durante una hora específica del día. 
#Ahora cree una lista N con el promedio diario de los resultados
#emulados de hacer las mediciones durante 30 días.
#Calcule la desviación estándar de los promedios diarios.

Measurements = [np.random.poisson(10, 60).sum() for x in range(24)]


N = [sum([np.random.poisson(10, 60).sum() for x in range(24)]) for x in range(30)]
N_new = list(np.random.poisson(10, 60*24*30))
sigma = np.array(N).std()

#Si sabemos que las estaturas de cierta población se distribuyen de forma normal 
#con una media de 1.68 m y una desviación estándar de 0.14 m.
#Genere una lista aleatoria Q para emular una muestra de 500 personas.
# ¿Cuál es la estatura promedio de la muestra? 
#¿Cuál fue la menor y la mayor estatura obtenida?

Q = list(np.random.normal(1.68, 0.14, 500))

mean = sum(Q)/len(Q)
std = np.array(Q).std()

#Los valores del largo de barras de metal en una fábrica están entre 80 y 90 cm.
#El valor esperado del largo de una barra es de 83 cm y se sabe que
#las probabilidades a partir de este valor a los extremos decrecen linealmente.
#Genere un histograma con 10 clases a partir de la emulación 
#de una muestra aleatoria de 10,000 barras.

triangular = np.random.triangular(80,83,90, 10000)
plt.hist(triangular, 10)
plt.show()
#Para hacer una comparación entre la distribución exponencial
# y la distribución gamma, genere una lista de 10000 muestras exponenciales
#con media 10, y otra con 10000 muestras gamma con α =2 y β=5. 
#Dibuje los histogramas de ambas en la misma gráfica
# y el mismo número de barras. ¿Qué observa?

Exponential = np.random.exponential(10, 10000)
Gamma = np.random.gamma(2, 5, 10000)
plt.hist((Exponential, Gamma), color=('b', 'g'), label=('exponential', 'gamma'))
plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
plt.show()
'''
I notice that at alpha = 1 the gamma function behaves like exponential (both decreasing) however
if I increase the alpha , it increases till 2nd bar and then decreases 
but as we increase more like alpha = 10 it increases till 3rd bar and then
decreases while exponential keeps on decreases from 1st bar
'''


