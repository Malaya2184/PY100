from locale import currency


class node :
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
class linkedList:
    def __init__(self):
        self.head = None
    def insertnode(self,data):
        
        newnode = node(data)
        
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                
            current.next =  newnode
            
    def printLinkedList(self):
        current = self.head
        while current is not None:
            print(current.data,"------>", end="")
            current = current.next
        print(None)

l = linkedList()
l.insertnode(5)
l.printLinkedList()
l.insertnode(9)
l.printLinkedList()