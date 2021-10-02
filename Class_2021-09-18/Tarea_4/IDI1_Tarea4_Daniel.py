# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:24:44 2021

@author: Act. Daniel Lagunas Barba
"""

import numpy as np
import collections
import matplotlib.pyplot as plt

#%% 1. En el juego Calabozos y dragones se usan dados no cÃºbicos. Suponga que tiene dados en
# forma de octaedro cuyas caras marcan 1,2,2,3,4,6,10,12. Emule el experimento de obtener la
# suma de dos de esos dados, genere una lista aleatoria L con los resultados de 1000 lanzamientos.
# Imprima el resultado que más se obtuvo en el experimento y el que menos.
Dado_CyD = [1,2,2,3,4,6,10,12]
L = list(np.random.choice(Dado_CyD, 1000, True) + np.random.choice(Dado_CyD, 1000, True))
Resultados = collections.Counter(L)
for _ in Resultados:
    if Resultados[_] == max(Resultados.values()):
        MaxRes = _
    elif Resultados[_] == min(Resultados.values()):
        MinRes = _
print(f'El resultado que más se obtuvo fue: {MaxRes} y el que menos se obtuvo fue: {MinRes}')

#%% 2. Suponga que tiene una baraja que tiene las cartas numeradas del 1 al 10 de cuatro colores
# distintos (azul, rojo, verde y amarillo), es decir, 40 cartas en total. Emule el proceso de
# repartir 5 cartas a un jugador. Repita el proceso 5000 veces e imprima según este experimento,
# ¿qué tan probable es obtener un juego que sume más de 30 puntos?
Azul = Rojo = Verde = Amarillo = np.arange(1, 11)
Baraja = np.concatenate((Azul, Rojo, Verde, Amarillo))
Em_rc = [np.random.choice(Baraja, 5, 'False') for i in range(5000)]
Em_rc_sumas = np.sum(Em_rc, axis=1)
Em_rc_sumas_gt30 = Em_rc_sumas[Em_rc_sumas > 30]
print(f'La probabilidad estimada de obtener un juego que sume más de 30 puntos es {100*len(Em_rc_sumas_gt30)/len(Em_rc)}%')

#%% 3. Emule el evento de contestar un examen de 12 preguntas, cada una de 4 opciones (sólo una
# correcta). Entregue una lista M con las calificaciones (sobre 100) de 500 exámenes contestados
# aleatoriamente.
M = list(np.random.binomial(12, 1/4, 500)/.12)

#%% 4. Se sabe que durante un turno de una fábrica se producen 10 pelotas cada minuto en promedio.
# Emule aleatoriamente los resultados de tomar mediciones cada minuto durante una hora específica
# del dí­a. Ahora cree una lista N con el promedio diario de los resultados emulados de hacer las
# mediciones durante 30 dí­as. Calcule la desviación estándar de los promedios diarios.
Em_mediciones = np.random.poisson(10, 60)
N = list(np.random.poisson(10, 60*24).mean() for x in range(30))
std_N = np.std(N)

#%% 5. Si sabemos que las estaturas de cierta población se distribuyen de forma normal con una
# media de 1.68m y una desviación estándar de 0.14 m. Genere una lista aleatoria Q para emular
# una muestra de 500 personas. ¿Cuál es la estatura promedio de la muestra? ¿Cuál fue la menor y
# la mayor estatura obtenida?
Q = list(np.random.normal(1.68, 0.14, 500))
print(f'La estatura promedio de la muestra es:{np.mean(Q): .2f}m')
print(f'La menor estatura de la muestra es:{np.min(Q): .2f}m, y la mayor:{np.max(Q): .2f}m')

#%% 6. Los valores del largo de barras de metal en una fábrica están entre 80 y 90 cm. El valor
# esperado del largo de una barra es de 83 cm y se sabe que las probabilidades a partir de este
# valor a los extremos decrecen linealmente. Genere un histograma con 10 clases a partir de la
# emulación de una muestra aleatoria de 10,000 barras.
muestra_barras_triangular = np.random.triangular(80, 83, 90, 10000)
plt.hist(muestra_barras_triangular, 10)
plt.show()

#%% 7. Para hacer una comparación entre la distribución exponencial y la distribución gamma,
# genere una lista de 10000 muestras exponenciales con media 10, y otra con 10000 muestras
# gamma con α=2 y β=5. Dibuje los histogramas de ambas en la misma gráfica y el mismo número
# de barras. ¿Qué observa?
m_exp = list(np.random.exponential(10, 10000))
m_gamma = list(np.random.gamma(2, 5, 10000))
plt.hist((m_exp, m_gamma))
plt.show()
'''
Se observa un parecido entre las distribuciones, indagando un poco encontré que la función
exponencial es un caso particular de la gamma cuando α=1.
'''