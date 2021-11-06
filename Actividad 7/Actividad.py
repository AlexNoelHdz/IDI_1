from cola_alex import cola

# Usando la clase nodo:
    # Escriba un método que devuelva la suma total de los nodos de un árbol recorriéndolo por profundidad.
# Ahora, escriba un método que de nuevo devuelva la suma total pero recorriendo el árbol por amplitud.
# Por último, escriba un método que imprima un árbol por amplitud.
# Ahora genere el siguiente árbol binario manualmente: (imagen en Canvas)
# Aplique sus funciones con el árbol anterior para verificar.  (En el caso de la función que imprime debería obtenerse: 2 5 7 1 4 3 6)
class nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izq=None
        self.der=None
    
    def suma_nodos(self):
        suma = self.dato 
            
        if self.izq is not None:
            suma += self.izq.suma_nodos()
    
        if  self.der is not None:
            suma += self.der.suma_nodos()
        
        return suma
    
    def suma_nodos_amplitud(self):
        auxiliar =  cola()
        auxiliar.enqueue(self)
        suma = 0
        while not auxiliar.empty():
            actual = auxiliar.dequeue()
            suma += actual.dato
            if actual.izq is not None:
                auxiliar.enqueue(actual.izq)
       
            if actual.der is not None:
                auxiliar.enqueue(actual.der)
        return suma
    
    def imprimir_amplitud(self):
        auxiliar = cola()
        auxiliar.enqueue(self)
        
        while not auxiliar.empty():
            actual=auxiliar.dequeue()
            print(actual.dato)
            if actual.izq is not None:
                auxiliar.enqueue(actual.izq)

            if actual.der is not None:
                auxiliar.enqueue(actual.der)
                
arbolito = nodo(2)
arbolito.izq = nodo(5)
arbolito.izq.izq = nodo(1)
arbolito.izq.der = nodo(4)
arbolito.der = nodo(7)
arbolito.der.izq = nodo(3)
arbolito.der.der = nodo(6)

suma_total = arbolito.suma_nodos()
suma_total_amplitud = arbolito.suma_nodos_amplitud()
arbolito.imprimir_amplitud()