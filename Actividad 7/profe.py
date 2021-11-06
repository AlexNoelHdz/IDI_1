# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:03:47 2021

@author: anhernan
"""
from cola_alex import cola

class nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izq=None
        self.der=None
        
    def buscar(self,que):
        if self.dato==que:
            return True
        if self.izq is not None:
            if self.izq.buscar(que):
                return True
        if self.der is not None:
            if self.der.buscar(que):
                return True
        return False
    
    def imprimir(self):
        print(self.dato)
            
        if self.izq is not None:
            self.izq.imprimir()
    
        if self.der is not None:
            self.der.imprimir()
            
    def imprimirA(self):
        auxiliar=cola()
        auxiliar.enqueue(self)
        
        while not auxiliar.empty():
            actual=auxiliar.dequeue()
            print(actual.dato)
            if actual.izq is not None:
                auxiliar.enqueue(actual.izq)

            if actual.der is not None:
                auxiliar.enqueue(actual.der)

    def contarA(self):
         auxiliar=cola()
         auxiliar.enqueue(self)
         cuenta=0
         while not auxiliar.empty():
             actual=auxiliar.dequeue()
             cuenta+=1
             if actual.izq is not None:
                 auxiliar.enqueue(actual.izq)
        
             if actual.der is not None:
                 auxiliar.enqueue(actual.der)
         
         return cuenta

    def contar(self):
        cuenta=1
        if self.izq is not None:
            cuenta+=self.izq.contar()
                
        if self.der is not None:
            cuenta+=self.der.contar()
                
        return cuenta
    
raiz=nodo(1)
raiz.izq=nodo(2)
raiz.der=nodo(3)
raiz.izq.izq=nodo(4)
raiz.izq.der=nodo(5)
raiz.izq.der.izq=nodo(8)
raiz.izq.der.der=nodo(9)
raiz.imprimirA()
X=raiz.contar()