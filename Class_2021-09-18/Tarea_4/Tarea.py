# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernandez
"""
import numpy as np
# import matplotlib.pyplot as pl
np.random.seed(666)


# 1. En el juego Calabozos y dragones se usan dados no cúbicos. 
# Suponga que tiene dados en forma de octaedro cuyas caras marcan 1,2,2,3,4,6,10,12. 
# Emule el experimento de obtener la suma de dos de esos dados, genere una lista aleatoria L con los resultados de 1000 lanzamientos. 
# Imprima el resultado que más se obtuvo en el experimento y el que menos.
L = [np.random.choice([1,2,2,3,4,6,10,12], 2).sum() for i in range(1000)]
print(f"Resultado más obtenido: {max(set(L), key = L.count)}")
print(f"Resultado menos obtenido: {min(set(L), key = L.count)}")
# 2. Suponga que tiene una baraja que tiene las cartas numeradas del 1 al 10 de cuatro colores distintos 
# (azul, rojo, verde y amarillo), es decir, 40 cartas en total. 
# Emule el proceso de repartir 5 cartas a un jugador. 
# Repita el proceso 5000 veces e imprima según este experimento, ¿qué tan probable es obtener un juego que sume más de 30 puntos?
Cartas = np.array([[1,2,3,4,5,6,7,8,9,10] for i in ["azul", "rojo", "verde","amarillo"]])
M = [np.random.choice(Cartas,5) for i in range(5000)]

# 3. Emule el evento de contestar un examen de 12 preguntas, cada una de 4 opciones (sólo una correcta). 
# Entregue una lista M con las calificaciones (sobre 100) de 500 exámenes contestados aleatoriamente.




# 4. Se sabe que durante un turno de una fábrica se producen 10 pelotas cada minuto en promedio. Emule aleatoriamente los resultados de tomar mediciones cada minuto durante una hora específica del día. 
# Ahora cree una lista N con el promedio diario de los resultados emulados de hacer las mediciones durante 30 días. Calcule la desviación estándar de los promedios diarios.




# 5. Si sabemos que las estaturas de cierta población se distribuyen de forma normal con una media de 1.68 m y una desviación estándar de 0.14 m. 
# Genere una lista aleatoria Q para emular una muestra de 500 personas. ¿Cuál es la estatura promedio de la muestra? ¿Cuál fue la menor y la mayor estatura obtenida?



# 6. Los valores del largo de barras de metal en una fábrica están entre 80 y 90 cm. 
# El valor esperado del largo de una barra es de 83 cm y se sabe que las probabilidades a partir de este valor a los extremos decrecen linealmente. 
# Genere un histograma con 10 clases a partir de la emulación de una muestra aleatoria de 10,000 barras.



# 7. Para hacer una comparación entre la distribución exponencial y la distribución gamma, 
# genere una lista de 10000 muestras exponenciales con media 10, y otra con 10000 muestras gamma con α =2 y β=5. 
# Dibuje los histogramas de ambas en la misma gráfica y el mismo número de barras. ¿Qué observa?