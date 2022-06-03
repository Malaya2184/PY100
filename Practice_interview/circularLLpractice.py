from requests import head


class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class circularLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertNode(self,data):
        
        newnode = node(data)
        
        if self.head is None:
            
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            tail = self.tail
            tail.next = newnode
            self.tail = tail.next
            
    def printCLL(self):
        current = self.head
        
        while current.next is not None and current.next is not self.head:
            print(current.data, end="----")
            current = current.next
        print(current.data)
        
    def reverseCLL(self):
        
        head = self.head
        tail = self.tail
        
        if head == tail:
            return
        else:
            count = 0
            while head.next is not tail:
                count+=1
                if count ==1:
                    prev = head
                    next = head.next
                    head.next = self.tail
                    self.tail = head
                    self.head = head.next
                    head = next
                else:
                    prev = head
                    next = head.next
                    head.next = prev
                    head = next
            tail.next = head
            
        
c = circularLL()
c.insertNode(1)
c.printCLL()
c.insertNode(2)
c.insertNode(3)
c.insertNode(4)
c.insertNode(5)
c.insertNode(6)
c.printCLL()
c.reverseCLL()
c.printCLL()