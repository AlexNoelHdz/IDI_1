# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:20:43 2021

@author: anhernan
"""

# Escriba funciones que reciban el nodo raíz de un árbol binario y, usando búsqueda por profundidad:

    # devuelva el valor máximo de los nodos del árbol
    # reciba un número y devuelva un booleano que indica si el dato está en el árbol
    # reciba un número y devuelva la cantidad de veces que aparece en el árbol
    # Ahora, escriba una función que reciba un entero y lo busque por amplitud 
    # en el árbol que tiene como raíz el nodo que llamó la función. 
    # a función devuelve el número de nodos que fueron revisados 
    # hasta encontrarlo, si el nodo no está devuelve la cantidad total de nodos en el árbol.
    
    # Después, realice una función dentro de la clase nodo que reciba un entero 
    # N>0 y genere un árbol a partir del nodo que llama la función, 
    # que contenga como datos los primeros N números primos colocados 
    # por amplitud en un árbol binario. Por ejemplo, si N=4 se genera el árbol 

from cola_alex import cola
def is_prime(num):
        if num > 1:  
            for n in range(2,num):  
                if (num % n) == 0:  
                    return False
            return True
        else:
            return False
    
def n_primes(n):
    i = 2
    primes = []
    while len(primes) < n:
        is_i_prime = is_prime(i)
        if is_i_prime:
            primes.append(i)
        i += 1
    return primes

class nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izq=None
        self.der=None
                
    def valor_max_nodo(self):
        valor_itself = self.dato
        valor_izq = 0 
        valor_der = 0
            
        if self.izq is not None:
            valor_izq = self.izq.valor_max_nodo()
    
        if  self.der is not None:
            valor_der = self.der.valor_max_nodo()
        
        return max(valor_itself,valor_izq,valor_der)
    
    def contains(self, num):
        if (self.dato == num):
            return True
            
        if self.izq is not None:
            if self.izq.contains(num):
                return True
            
        if  self.der is not None:
            if self.der.contains(num):
                return True
        
        return False
    
    def count(self, num):
        n = 0
        if (self.dato == num):
            n += 1
            
        if self.izq is not None:
            n +=  self.izq.count(num)
            
        if  self.der is not None:
            n +=  self.der.count(num)
        
        return n
    
    def search_cost_amplitud(self, num):
        auxiliar =  cola()
        auxiliar.enqueue(self)
        cost = 0
        while not auxiliar.empty():
            actual = auxiliar.dequeue()
            cost += 1
            if actual.dato == num:
                break;
                
            if actual.izq is not None:
                auxiliar.enqueue(actual.izq)
       
            if actual.der is not None:
                auxiliar.enqueue(actual.der)

        return cost
        
    def create_primes_tree(self, n):
        primes = n_primes(n)
        self.dato = primes[0]
        level = 1
        
        auxiliar = cola()
        auxiliar.enqueue(self)
    
        while level < n:
            actual = auxiliar.dequeue()
            
            if actual.izq is None and level < n:
                actual.izq = nodo(primes[level])
                level += 1
                auxiliar.enqueue(actual.izq)
                
            if actual.der is None and level < n:
                actual.der = nodo(primes[level])
                level += 1
                auxiliar.enqueue(actual.der)
    
tree_4 = nodo(None)
tree_4.create_primes_tree(4)
tree_7 = nodo(None)
tree_7.create_primes_tree(7)


