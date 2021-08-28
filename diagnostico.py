# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 21:12:11 2021

@author: Alejandro Hernandez
"""
# mayor: recibe tres números reales y devuelve el valor máximo entre los 3
def mayor(num1, num2, num3):
    return max(num1, num2, num3)

print(f"Entre 5,3,2 el mayor es {mayor(5,3,2)}")

# maymen: recibe una lista numérica y un booleano. Si el booleano es True devuelve el
# máximo de la lista, sino el mínimo. El booleano es opcional y por defecto es True 

def mayMen(numbers, max_value = True):
    if(max_value):
        min(numbers)
    return max(numbers)

numbers = [5,3,2,10]
print(f"Entre {numbers} el mayMen es {mayMen(numbers)}")

# triangular: recibe un número natural y devuelve un booleano que indica si el número es
# triangular o no
def triangular(n):
    t_n = 0
    i = 1
    while (t_n < n):
        t_n = (i * (i + 1)) / 2
        if(n == t_n):
            return True
        i += 1
        return False
triangular(3)

        
# listamult: recibe dos números enteros n>=1, a>=2 y devuelve una lista con los primeros n
# números naturales múltiplos de a
def listamult(n, a):
    if(n >= 1 and a >= 2 and isinstance(n, int) and isinstance(a, int) ):
        #Do stuff
        lista = []
        for i in range(1, n):
            lista.append(i*a)
        return lista    
    raise Exception("n y a tienen que ser números enteros con los siguientes criterios: n>=1, a>=2")

listamult(10, 3)

# perfecto: recibe un número n y devuelve un booleano indicando si el número es perfecto
# o no

# coprimos: recibe dos números naturales y devuelve un booleano que indica si son primos
# relativos o no

# extrae: recibe una lista numérica L y un número n, devuelve una lista con los elementos de
# L mayores a n

# primos: recibe un número natural mayor o igual a 2 y devuelve la cantidad de números
# primos entre 2 y el número dado.