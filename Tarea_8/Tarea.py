# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:19:32 2021

@author: anhernan
"""

#%%Genere una clase pila que incluya:
    # propiedad data (lista con la información incluida en la pila)
    # propiedad capacity (entero que indica el número máximo de elementos que puede tener la pila)
    # constructor que inicializa la lista data como vacía y recibe un entero para la capacidad (opcional, por defecto 100)
    # método push que inserta un elemento en el "tope" de la pila (si está llena ignora la llamada)
    # método pop que quita y devuelve el elemento en el "tope" de la pila (no previene si la pila está vacía)
    # método peek que devuelve sin sacar el elemento en el "tope" de la pila (no previene si la pila está vacía)
    # método empty que devuelve un booleano en función de si la pila está vacía o no
    # método full que devuelve un booleano en función de si la pila está llena o no
    # método count que devuelve la cantidad de elementos actual en la pila
    # método print que imprime la pila en el orden que se insertaron los datos

class pila:
    
    def __init__(self, capacity = 100):
        self.data = []
        self.capacity = capacity
    
    def push(self, element):
        if not self.full():
            self.data.append(element)
    
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def empty(self):
        return (self.count()== 0)
    
    def full(self):
        return (self.count() == self.capacity)
            
    def count(self):
        return len(self.data)

    def print(self):
        for element in self.data:
            print(element)
        
#%% Genere una clase cola que incluya:

    # propiedad data (lista con la información incluida en la cola)
    # propiedad capacity (entero que indica el número máximo de elementos que puede tener la cola)
    # constructor que inicializa la lista data como vacía y recibe un entero para la capacidad (opcional, por defecto 100)
    # método enqueue que inserta un elemento al "final" de la cola (si está llena ignora la llamada)
    # método dequeue que quita y devuelve el elemento al "inicio" de la cola (no previene si la cola está vacía)
    # método peek que devuelve sin sacar el elemento al "inicio" de la cola (no previene si la cola está vacía)
    # método empty que devuelve un booleano en función de si la cola está vacía o no
    # método full que devuelve un booleano en función de si la cola está llena o no
    # método count que devuelve la cantidad de elementos actual en la cola
    # método print que imprime la cola en el orden que se insertaron los datos
class cola:
    
    def __init__(self, capacity = 100):
        self.data = []
        self.capacity = capacity
    
    def enqueue(self, element):
        if not self.full():
            self.data.insert(0, element)
    
    def dequeue(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def empty(self):
        return (self.count()== 0)
    
    def full(self):
        return (self.count() == self.capacity)
            
    def count(self):
        return len(self.data)

    def print(self):
        for element in self.data[::-1]:
            print(element)

#%% Ahora use sus clases para generar una pila llamada pila1 de capacidad 50 en la que se apilen los primeros 50 números naturales impares.
pila1 = pila(50)
for impar in [i for i in range(100) if i % 2 != 0]:
    pila1.push(impar)
# Ahora cree una cola llamada cola1 de capacidad 50 y encole los elementos de la pila1
cola1 = cola(50)
for element in pila1.data:
    cola1.enqueue(element)
# Imprima ambas estructuras para comprobar.
print("#%% Pila:")
pila1.print()
print("#%% Cola:")
cola1.print()


#%%