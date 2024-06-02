class _Node:
    __slots__ = '_element','_next','_prev'

    def __init__(self,element):
        self._element = element
        self._next = None
        self._prev = None

class CircularLinkedList:
    def __init__(self):
        self._tail = None

    def is_empty(self):
        return self._tail is None

    def add_first(self,element):
        new_node = _Node(element)
        if self.is_empty():
            new_node._next = new_node
            self._tail = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node

    def add_last(self, element):
        self.add_first(element)
        self._tail = self._tail._next
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError("list is empty")
        if self._tail._next is self._tail:
            self._tail = None
        else:
            self._tail._next = self._tail._next._next
            removed_element = self._tail._next._next
            return removed_element
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("list is empty")
        current = self._tail._next
        if self._tail._next is self._tail:
            self._tail = None
            return self._tail
        while current._next is not self._tail:
            current = current._next
        self._tail = current
        self._tail._next = current._next._next

    def remove_anypos(self, pos):
        if self.is_empty():
            raise IndexError("list is empty")
        if pos == 0:
            self.remove_first()
        current = self._tail._next
        while pos > 1:
            current = current._next
            pos -= 1
        current._next = current._next._next
        removed_element = current._next._element

        if current._next == self._tail._next:
            self._tail = current
        return removed_element
    
    def second_last(self):
        if self.is_empty():
            raise IndexError("list is empty")
        current = self._tail._next
        while current is not self._tail:
            current = current._next
            if current._next is self._tail:
                return current._element
        
    def count(self,temp):
        if temp._next is self._tail:
            return 1
        else:
            return 1 + self.count(temp._next)
    
    def concatenate(self,a,b):
        if a.is_empty():
            return b
        elif b.is_empty():
            return a
        else:
            temp = a._tail._next
            a._tail._next = b._tail._next 
            b._tail._next = temp
            self._tail = b._tail
            self.display()
        
    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self._tail._next
        while current is not self._tail:
            print(current._element, end=' -> ')
            current = current._next
        print(self._tail._element)

clist = CircularLinkedList()
blist = CircularLinkedList()
clist.add_first(9)
clist.add_first(11)
clist.add_first(7)
clist.add_first(90)
clist.add_last(98)

blist.add_first(9)
blist.add_first(11)
blist.add_first(7)
clist.concatenate(clist,blist)
print("second to last", clist.second_last())
print(clist.count(clist._tail))
class DoublyLinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
    def is_empty(self):
        return self._tail is None and self._head is None

    def add_element(self,element):
        new_node = _Node(element)
        if self.is_empty():
            new_node._next = new_node
            new_node._prev = new_node
            self._tail = new_node
            self._head = new_node
        new_node._prev = self._tail
        new_node._next = self._head
        self._head._prev = new_node
        self._tail._next = new_node
        self._tail = new_node

    def add_first(self,element):
        if self.is_empty():
            return self.add_element(element)
        new_node = _Node(element)
        new_node._next = self._head
        new_node._prev = self._tail
        self._head._prev = new_node
        self._tail._next = new_node
        self._head = new_node
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError("list is empty")
        removed_element = self._head._element
        if self._head is self._tail:  # Check if there's only one node
            self._head = None
            self._tail = None
        self._tail._next = self._head._next
        self._head = self._head._next
        self._head._prev = self._tail
        return removed_element
    
    def remove_anypos(self,pos):
        if self.is_empty():
            raise IndexError("list is empty")
        if pos == 1:
            return self.remove_first()
        else:
            current = self._head
            for _ in range(pos-1):
                current = current._next
        current._prev._next = current._next
        if current._next._prev is self._tail:
            self._tail = current._prev
        current._next._prev = current._prev
        removed_element = current._element
        print("removed element", removed_element)

    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self._tail._next
        while current is not self._tail:
            print(current._element, end=' <-> ')
            current = current._next
        
        print(self._tail._element)


clist = DoublyLinkedList()
clist.add_element(6)
clist.add_element(4)
clist.add_element(3)
clist.add_first(10)
clist.add_element(8)
clist.add_first(9)
clist.display()
clist.remove_anypos(4)


clist.display()