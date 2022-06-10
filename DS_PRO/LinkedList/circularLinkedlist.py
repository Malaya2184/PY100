from multiprocessing.connection import wait


class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertNode(self, data):
        
        newnode = node(data)
        
        
        if self.tail is None:
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.tail.next = newnode
            self.tail = self.tail.next
            
    def printCLL(self):
        head = self.head
        tail = self.tail
        while head.next is not None and head.next is not tail:
            print(head.data, end="---")
            head = head.next
        print(head.data, end="---")
        print(tail.data)
        
    def printTail(self):
        print('tail data', self.tail.data)
        print('tail next data', self.tail.next.data)
        
c = circularLinkedList()
c.insertNode(1)
c.insertNode(1)
c.insertNode(3)
c.insertNode(4)
c.insertNode(5)
c.printCLL()
c.printTail()