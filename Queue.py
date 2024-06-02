class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.data[self.front]
    
    def enqueue(self, e):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1
    
    def resize(self,cap):
        old = self.dataself.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        answer = self.data[self.front]
        self.data = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer