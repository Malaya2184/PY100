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
                count +=1
                if count ==1:
                    next = head.next
                    prev = head
                    head.next = tail
                    newtail = head
                    head = next
                else:
                    next = head.next
                    head.next = prev
                    prev = head
                    head = next
            if count is not 0:
                next = head.next
                head.next = prev
                prev = head
                tail.next = prev
                self.head = tail
                self.tail = newtail
            else:
                head.next = tail
                self.tail.next = head
                self.head = tail
                self.tail = head          
                    
               
            
                  
            
        
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