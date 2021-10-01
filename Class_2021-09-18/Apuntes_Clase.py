# -*- coding: utf-8 -*-
"""
@author: Alejandro Hernandez
Distribuciones de probabilidad discretas y continuas

Discretas: 
    La variables son contables. 
    Discreto brinca en puntos aislados.
    
Continuas:
    Las variables son medibles.

Binomial: 
    Las probabilidades no se ven afectadas si repites el proceso.
    Hay una probabilidad fija de éxito cada vez que repites el proceso.
    Cuando tiras un dado tienes 50% de probabilidades de par o un par.
Tarea apareceran 6 distribuciones
"""

import numpy as np
import matplotlib.pyplot as pl
np.random.seed(100)


#si tengo un 1/6 de probabilidades de que me salga un 1 cómo se comportaría al medirlo 10 veces?
# x = np.random.binomial(10, 1/6)
#n= cuantas veces repites el experimento. P = probabilidad.
# x = np.random.binomial(10, 0.5)
#pedir un arreglo. 20 veces tirar 10 veces un dado. 
#Si tienes 50% de probabilidad tiene que centrarse más en el 5
#Por ejemplo la suma de dos dados.
# x = np.random.binomial(10, 0.5, 20)
#Hacer el proceso con 1000
#Se tiene ya la distribución de probabilidad,
#una vez que existe modelamos el resultado:
#Primer numero: Cuántas veces repites el proceso.
#Si tirar dados es binomial
#Y cada que lo tiras es 50% (.5)
#Así se modela tirar 100000 una moneda:
#tirando 10 veces moneda y repitiendolo 10000 veces.
x = np.random.binomial(10, 0.5, 10000)

#ver gráficamente la distribución binomial
#Es parecida a la campana de Gauss
#Con un histograma (gráfica de distribuciones de frecuencia)
#Dos maneras, boton derecho -> Histogram
#Esta versión no tiene mucho control de cómo se hace el histograma
#EL histograma no es predecible en lo local pero sí en lo global
#La forma del histograma es constante según el experimento
#Entre más se repite el experimento más se respeta la distribución
#Geométricamente se ve más simétrico con 10000 que con 1000

#Distribución de Poisson
#P.e. promedio de 5.8 cajas por hora
# y = np.random.poisson(5.8)
#10 000 veces con un promedio de 5.8
# y = np.random.poisson(5.8, 10000)
#Llegan 20 personas al oxxo cada hora:
#Simulación aleatoria de repetir mismo experimento 24 veces
#Porque hay 24 horas
y = np.random.poisson(20, 24)

#distribución continua
#La más común es la normal
#Se está emulando un experimento que tiene valores continuos
#Argumentos: promedio, desviación estandar (cuanto te alejas izquierda derecha)
#Se relaciona con el teorema de Chebyshev
#Proceso con promedio de 50 desviación estandar de 10
# z = np.random.normal(50, 10)
#repetir el experimento 10000 veces
# z = np.random.normal(50, 10, 10000)

#Emular estaturas de un millón de personas promedio de 1.72
#Segundo parámetro desviación estandar
z = np.random.normal(1.72, 0.15, 1000000)
w = np.random.normal(1.71, 0.13, 1000000)
#===Histogramas===#
#bins: barras
#hist te puede regresar los datos necesarios para el histograma
#Regresa 3 datos 
    # 1. Contador de apariciones en barras (frecuencias)
    # 2. Extremos de las clases. Rango de las barras ejemplo 14-15.3636
    # 3. Información de coordenadas gráficas
# a = pl.hist(x, 11)
#Si le pido sobre poisson
# a = pl.hist(y, 11)
#Guardar en variables independientes y usar z (estaturas)
# a, b, _ = pl.hist(z, 5)
#Entre más barras más parece campana de Gauss
# a, b, _ = pl.hist(z, 50)

#Pedir dos conjuntos de datos en mismo histograma
a, b, _ = pl.hist((z, w), 5)


















