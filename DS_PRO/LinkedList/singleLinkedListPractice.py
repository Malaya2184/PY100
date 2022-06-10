class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class singleList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
            
    def print(self):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                print(current.data, end='---->')
                current = current.next
            print(current.data, '---->None')
        else:
            print('There is no linkedlist to print')
    
    def insertMulti(self,arr):
        current = self.head
        for i in arr:
            self.insert(i)
            

        
        
s=singleList()
s.print()
s.insert(1)
s.insert(2)
s.insertMulti([3,4,5])
s.print()
s1=singleList()
s1.print()
s1.insert(1)
s1.insert(2)
s1.insertMulti([3,4,5])
s1.print()


