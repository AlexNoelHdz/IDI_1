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