class _Node:
    __stack__= '_element','_next'
    def __init__(self,element):
        self._element = element
        self._next = None
class _Queue:
    def __init__(self):
        self._rear = None
        self._front = None
        self._size = 0
    
    def is_empty(self):
        return self._size == 0

    def enqueue(self,element):
        newest = _Node(element)
        if self.is_empty():
            self._front = newest
            self._rear = newest
            self._size += 1
        else:
            self._rear._next = newest
            self._rear = newest
            self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        element = self._front._element
        self._front = self._front._next
        self._size -= 1
        return element
    
    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self._front._element
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        current = self._front
        while current:
            print(current._element, end=' -> ')
            current = current._next
        print()

queue = _Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
print(queue.peek())
queue.display()