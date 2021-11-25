# -*- coding: utf-8 -*-
"""
@author: anhernan
"""
def tupla_min_max(izq, der, tipo):
       if tipo == True:
           if izq.dato >= der.dato:
               return izq, 'IZQUIERDA'
           return der, 'DERECHA'
       else:
           if izq.dato <= der.dato:
               return izq, 'IZQUIERDA'      
           return der, 'DERECHA' 
           
class nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izq=None
        self.der=None
                
    def min_max(self, tipo = True, prof = 1):
            # print(self.dato)
            #Nada en hijos o profundidad no mayor que 1
            if (self.izq is None and self.der is None) or not prof > 1:
                return self, 'RAIZ'
            
            #Caso desbalanceado 1
            if (self.izq is None and self.der is not None):
                return self.der.min_max(not tipo, prof-1)
            #Caso desbalanceado 2
            if (self.izq is not None and self.der is None):
                return self.izq.min_max(not tipo, prof-1)
            
            
            nodo_izq, _ = self.izq.min_max(not tipo, prof-1)
            nodo_der, _ = self.der.min_max(not tipo, prof-1)
        
                
            return tupla_min_max(nodo_izq, nodo_der, tipo)
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
nodo, lado = arbolito.min_max(True, 4)
print(nodo.dato, lado)
nodo, lado =  arbolito.min_max(False, 4)
print(nodo.dato, lado)
nodo, lado =  arbolito.min_max(True, 3)
print(nodo.dato, lado)
nodo, lado =  arbolito.min_max(False, 3)
print(nodo.dato, lado)


