class _Node:
    __stack__= '_element','_next'
    def __init__(self,element):
        self._element = element
        self._next = None
        
class _Stack:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def is_empty(self):
        return  self._size == 0
        
    
    def push(self,element):
        newest = _Node(element)
        if self.is_empty():
            self._top = newest
            self._size += 1
        else:
            newest._next = self._top
            self._top = newest
            self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty!!")
        element = self._top._element
        self._top = self._top._next
        self._size -= 1
        return element
    
    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._top._element
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        
        current = self._top
        while current:
            print(current._element, end=' -> ')
            current = current._next
        print()

# matches delimiters
def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = _Stack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

print(is_matched('[(5+x)-([y+z])]'))