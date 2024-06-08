class PriorityQueueBase:
    class Item:
       
        def __init__(self,k,v):
            self.key = k
            self.value = v
        def __it__(self,other):
            return self.key < other.key
        
    def is_empty(self):
        return len(self) == 0

class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    def add(self,key,value):
        self.data.append(self.Item(key,value))
    
    def min(self):
        # return but don't remove
        if self.is_empty():
            raise ValueError("empty")
        small = self.data[0]
        small_index = 0
        for i,item in enumerate(self.data):
            if item.key < small.key:
                small = item
                small_index = i
        return (small.key, small.value), small_index
    
    def remove(self):
        if self.is_empty():
            raise ValueError("empty")
        
        mini, small_index = self.min()
        return self.data.pop(small_index).key, self.data.pop(small_index).value

class SortedPQ(PriorityQueueBase):
    def __init__(self):
        self.data = []

    def add(self, k, v):
        new_item = self.Item(k, v)
        if len(self.data) == 0:
            self.data.append(new_item)
        else:
            for i, item in enumerate(self.data):
                if new_item.key < item.key:
                    self.data.insert(i, new_item)
                    break
            else:
                # If we don't find a smaller key, we append it to the end
                self.data.append(new_item)
    
    def min(self):
        item = self.data[0]
        return item.key, item.value
    
    def remove(self):
        item = self.data.pop(0)
        return item.key, item.value
            

pq = SortedPQ()


pq.add(3,'ronaldo')
pq.add(2,'messi')
pq.add(5,'suarez')
print(pq.min())
print(pq.remove())