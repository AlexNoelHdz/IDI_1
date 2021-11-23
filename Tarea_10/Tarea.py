# -*- coding: utf-8 -*-
"""
@author: anhernan
"""
def tupla_min_max(izq, der, tipo):
       if tipo == True:
           return (max(izq, der), 'IZQUIERDA' if izq >= der else 'DERECHA')
           
       return (min(izq, der), 'IZQUIERDA' if izq <= der else 'DERECHA')
   
class nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izq=None
        self.der=None
                
    def min_max(self, tipo, prof):
        
            if (self.izq is None and self.der is None) or prof == 1:
                return self.dato, 'RAIZ'
            
            if self.izq is not None:
                value_izq = self.izq.min_max(prof-1, not tipo)
            if self.der is not None:
                value_der = self.der.min_max(prof-1, not tipo)
               
            return tupla_min_max(value_izq[0], value_der[0], tipo)
# %%MiniMax Arbol
# Level 1
arbolito = nodo(0)

# Level 2
arbolito.izq = nodo(4)

arbolito.der = nodo(9)

# Level 3
arbolito.izq.izq = nodo(5)
arbolito.izq.der = nodo(2)

arbolito.der.izq = nodo(1)
arbolito.der.der = nodo(-3)

# Level 4
arbolito.izq.izq.izq = nodo(7)
arbolito.izq.izq.der = nodo(3)
arbolito.izq.der.izq = nodo(4)
arbolito.izq.der.der = nodo(1)

arbolito.der.izq.izq = nodo(10)
arbolito.der.izq.der = nodo(2)
arbolito.der.der.izq = nodo(1)
arbolito.der.der.der = nodo(8)

# %%MinMax Tests
test = arbolito.min_max(True, 4)
print(test)
test = arbolito.min_max(False, 4)
print(test)
test = arbolito.min_max(True, 3)
print(test)
test = arbolito.min_max(False, 3)
print(test)


