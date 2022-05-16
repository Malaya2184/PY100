
class node :
    def __init__(self, data, left= None, right = None):
        self.data = data
        self.left = left
        self.right = right

class bst:
    def __init__(self):
        self.head = None
        
    def insertNode(self, data):
        
        newnode = node(data)
        
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            
            while current is not None:
                if data > current.data:
                    if current.right!=None:
                        current = current.right
                    else:
                        current.right=newnode
                        break
                else:
                    if current.left!=None:
                        current = current.left
                    else:
                        current.left=newnode
                        break
            current = newnode



bst = bst()
bst.insertNode(5)
bst.insertNode(10)
bst.insertNode(15)
bst.insertNode(2)
current = bst.head
print(current.data)
print(current.right.data)
print(current.right.right.data)
print(current.left.data)

    

        