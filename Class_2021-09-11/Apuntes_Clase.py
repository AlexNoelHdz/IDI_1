# -*- coding: utf-8 -*-
"""

@author: Alejandro Hernandez

===================Librería Random===================================
En Computación no existe el concepto de aleatorio refiriendose al azar

NUmpy incluye random dentro
Es muy común que en vez de importar random, utilices la implementación 
de Numpy
La computadora siempre hace un proceso determinista, por lo que cuesta
que los números sean realmente aleatorios.

Alan turin sugirió que la computadora brinde pseoudoaleatoriedad
Da la impresión de que es aleatorio, pero no lo es
Debe ser igual de probable que te dé cualquier número en el rango
Al inicio la computadora sacaba la hora del reloj y luego hacía una 
operación matemática compleja para entregar algo

Tiene que tomar algo inicial que si sea diferente cada vez
1.- Ahora combinan la hora y la mac adress del equipo (Es común)
2.- Revuelven esto y toman un 3er número (Semilla)
3.- La escencia es que toman como semilla este número para el nuevo
algorítmo de aleatoriedad.

Los aleatorios se pueden pedir en espacios continuos o discretos.

Continuo: Rango aleatorio de variables.

Discreto: Por ejemplo números enteros.

Las variables discretas hacen referencia a cosas que se cuentan, 
las continuas a cosas que se miden.

Usualmente las librerías aleatorias incluyen una función continua 
o discreta.

Cuando una variables en continua, un punto no tiene importancia
porque en realidad es infinita


===========Fuentes================
https://keycombiner.com/collections/spyder/
"""

import numpy as np

#Función continua random [0, 1) (no incluye el 1)
#La cantidad de números entre 0 y 1 es infinita y no numerable (no tiene sentido sumar)
# x = np.random.random()
#[0,2) -> Con esta lógica el último número tiene que ser par
# x = np.random.random() * 2
# [0, 2) -1 = [-1, 1)
# x = np.random.random() * 2 -1
#Probabilidad uniforme (Sigue siendo contínuo)
#Tienes un espacio definido y todos los valores son igualmente probables
#[-1, 1)
# x = np.random.uniform(-1,1)
#[-1, 1) Matriz
# x = np.random.uniform(-1,1,(6,3))
#Dos matrices
# x = np.random.uniform(-1,1,(2,2))
# y = np.random.uniform(-1,1,(2,2))
#Semilla es una manera de definir con qué número haces la operación
#Para que el algorítmo no tome como referencia otra cosa
#Por ejemplo la Hora
"""
#Si reseteas el Seed son los mismos números:
np.random.seed(100)
x = np.random.uniform(-1,1,(2,2))
np.random.seed(100)
y = np.random.uniform(-1,1,(2,2))
"""

# np.random.seed(300)
x = np.random.uniform(-1,1,(2,2))
# np.random.seed(100)
y = np.random.uniform(-1,1,(2,2))

#===Versión discreta===#
z = np.random.randint(3,9, (3,3))
#Segunda manera de hacerlo
#En vez de pedir número aleatorio
#Puedes definir: 
#Probabilidad uniforme no significa en cascada
#Selección con reemplazo: todas las selecciones tienen
#la misma probabilidad y pueden seguir saliendo
L=[2,5,11,27]
# w = np.random.choice(L, 3)
#Excluye los que ya salgan
# w = np.random.choice(L, 4,False)
#error por que ya no puede salir
# w = np.random.choice(L, 5,False)
#quitamos error
# w = np.random.choice(L, 5)
#Definimos probabilidades! 70% para el 2
# w = np.random.choice(L, 5,p=[0.7,0.1,0.1,0.1])
#Barajar o revolver 
np.random.shuffle(L)
#Algo similar pero no afecta L:
w = np.random.choice(L,4)


    

