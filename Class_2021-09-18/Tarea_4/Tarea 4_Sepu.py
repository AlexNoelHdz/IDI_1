import numpy as np
import matplotlib.pyplot as plt

#En el juego Calabozos y dragones se usan dados no cúbicos. Suponga que tiene 
#dados en forma de octaedro cuyas caras marcan 1,2,2,3,4,6,10,12. Emule el 
#experimento de obtener la suma de dos de esos dados, genere una lista 
#aleatoria L con los resultados de 1000 lanzamientos. Imprima el resultado que 
#más se obtuvo en el experimento y el que menos.

D_Octa = [1,2,3,4,5,5,6,7,8,9,10,11,12]

l = np.sum(np.random.choice(D_Octa,(2,1000)),0)
L = l.tolist()

print('Más Frecuente=  %d \nMenos Frecuente =  %d'\
      % (max(set(L), key=L.count),min(set(L), key=L.count)))

#-----------------------------------------------------------------------------

#Suponga que tiene una baraja que tiene las cartas numeradas del 1 al 10 de 
#cuatro colores distintos (azul, rojo, verde y amarillo), es decir, 40 cartas 
#en total. Emule el proceso de repartir 5 cartas a un jugador. Repita el 
#proceso 5000 veces e imprima según este experimento, ¿qué tan probable es 
#obtener un juego que sume más de 30 puntos?

#Seguro había otra manera de definir las 40 cartas
Cartas = [1,2,3,4,5,5,6,7,8,9,10,1,2,3,4,5,5,6,7,8,9,10,1,2,3,4,5,5,6,7,8,9,\
          10,1,2,3,4,5,5,6,7,8,9,10]

C = np.sum(np.random.choice(Cartas,(5,5000)),0)

PM30 = sum(1 for i in C if i > 30)/C.size*100
print(PM30)

#-----------------------------------------------------------------------------

#Emule el evento de contestar un examen de 12 preguntas, cada una de 4 opciones 
#(sólo una correcta). Entregue una lista M con las calificaciones (sobre 100) 
#de 500 exámenes contestados aleatoriamente.

#Whut?/ Se va hacer la prueba 12 veces con un 25% de probabilidad de exito 
#cada una por 500 veces. En ninguno de los casos da un 100%. No sé porque. 

M = np.random.binomial(12,0.25,500)
E100 = sum(1 for i in M if i == 12)/M.size*100
print("Examenes con 100 = %.5f " % E100)

#-----------------------------------------------------------------------------

#Se sabe que durante un turno de una fábrica se producen 10 pelotas cada minuto 
#en promedio. Emule aleatoriamente los resultados de tomar mediciones cada 
#minuto durante una hora específica del día. Ahora cree una lista N con el 
#promedio diario de los resultados emulados de hacer las mediciones durante 30 
#días. Calcule la desviación estándar de los promedios diarios.

N = []

for i in range(30):    
    N.append(np.mean(np.random.poisson(10,60)))

print("Desviación Estandar = %f" % np.std(N))

#-----------------------------------------------------------------------------

#Si sabemos que las estaturas de cierta población se distribuyen de forma 
#normal con una media de 1.68 m y una desviación estándar de 0.14 m. Genere una 
#lista aleatoria Q para emular una muestra de 500 personas. ¿Cuál es la 
#estatura promedio de la muestra? ¿Cuál fue la menor y la mayor estatura 
#obtenida?

Q = np.random.normal(1.68,0.14,500).tolist()

print("Promedio = %.2f" % np.mean(Q))
print("Menor = %.2f" % np.min(Q))
print("Mayor = %.2f" % np.max(Q))

#-----------------------------------------------------------------------------

#Los valores del largo de barras de metal en una fábrica están entre 80 y 90 cm. 
#El valor esperado del largo de una barra es de 83 cm y se sabe que las 
#probabilidades a partir de este valor a los extremos decrecen linealmente. 
#Genere un histograma con 10 clases a partir de la emulación de una muestra 
#aleatoria de 10,000 barras.

plt.hist([np.random.triangular(80,83,90) for i in range(10000)], bins = 10)


#-----------------------------------------------------------------------------

#Para hacer una comparación entre la distribución exponencial y la distribución 
#gamma, genere una lista de 10000 muestras exponenciales con media 10, y otra 
#con 10000 muestras gamma con α =2 y β=5. Dibuje los histogramas de ambas en 
#la misma gráfica y el mismo número de barras. ¿Qué observa?

D_Exp = plt.hist(np.random.exponential(10,10000), bins = 100)
D_Gam = plt.hist(np.random.gamma(2,5,10000), bins = 100)

#Se ve que la exponencial logra tener los valores más altos y un rango más 
#grande mientras que la gamma está mas centrada en su promedio y no tan
#dispersa.
