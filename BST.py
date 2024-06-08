print("hello world")
class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    def InOrderPrint(self):
        if self.left:
            self.left.InOrderPrint()
        print(self.data, end=" ")
        if self.right:
            self.right.InOrderPrint()

    def PreOrderPrint(self):
        print(self.data,end=' ')
        if self.left:
            self.left.PreOrderPrint()
        if self.right:
            self.right.PreOrderPrint()
    
    def PostOrderPrint(self):
        print(self.data, end=" ")
        if self.right:
            self.right.PostOrderPrint()
        if self.left:
            self.left.PostOrderPrint()
    
    def BFS(self):
        queue = []
        if self.data:
            queue.append(self.data)
            if self.left:
                queue.append(self.left.data)
            if self.right:
                queue.append(self.right.data)
        self.BFS()

    
        
if __name__ == '__main__':
    bt = Node(9)
    bt.insert(5)
    bt.insert(7)
    bt.insert(8)
    bt.insert(13)
    bt.insert(11)
    bt.insert(15)
    print("inorder: ", bt.InOrderPrint())
    print("preorder: ",bt.PreOrderPrint())
    print("post order: ",bt.PostOrderPrint())