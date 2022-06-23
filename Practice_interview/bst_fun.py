class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    
    def __init__(self):
        self.head = None
        
    def insertNode(self, data):
        
        newnode = node(data)
        
        if self.head is None:
            self.head = newnode
        else:
             current = self.head
             
             while current is not None:
                 
                 if data > current.data:
                     if current.right is None:
                         current.right = newnode
                         break
                     else:
                         current = current.right
                 else:
                     if current.left is None:
                         current.left =newnode
                         break
                         
                     else:
                         current = current.left
                         
                         
# printing level by level in bst
    def printBst(self,head):
        
        current = head
        if current == self.head:
            print(current.data)
        elif head is None:
            return

        if current.left is not None or current.right is not None:
            if current.left is not None:
                print(current.left.data)
            if current.right is not None:
                print(current.right.data)
            
        left = self.printBst(current.left)
        right = self.printBst(current.right)
        
        
b = BinarySearchTree()
b.insertNode(5)
b.insertNode(3)
b.insertNode(7)
b.insertNode(2)
b.insertNode(4)
b.insertNode(6)
b.insertNode(8)
b.insertNode(9)
b.insertNode(1)
print(b.head.data)
b.printBst(b.head)
            
                     
                     
            