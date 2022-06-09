class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, data):
        newnode = node(data)
        
        if self.head is None:
            self.head =  newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
    def printLL(self):
        
        current = self.head
        while current.next is not None:
            print(current.data, end='----->')
            current = current.next
        print(current.data, '------>None')
    def sortLL(self):
        arr=[]
        current = self.head
        while current.next is not None:
            arr.append(current.data)
            current = current.next
        arr.append(current.data)
        arr.sort()
        self.head = None
        
        for i in arr:
            self.insertNode(i)
            
def mergeTwoSortedLL(l, l2):
    
    current1 = l.head
    current2 = l2.head
    l3 = linkedList()
    
    while current1.next is not  None and current2.next is not None:
        if current1.data < current2.data:
            l3.insertNode(current1.data)
            current1 = current1.next
            current2 = current2
        else:
            l3.insertNode(current2.data)
            current2 = current2.next
            current1 = current1
            
    if current1.next is None:
            if current1.data < current2.data:
                l3.insertNode(current1.data)
                while current2.next is not None:
                    l3.insertNode(current2.data)
                    current2 = current2.next
                l3.insertNode(current2.data)
    else:
            if current2.data < current1.data:
                l3.insertNode(current2.data)
                while current1.next is not None:
                    l3.insertNode(current1.data)
                    current1 = current1.next
                l3.insertNode(current1.data)
    return l3
        
    
    
                 
                           
    
    
    
            
l = linkedList()
l.insertNode(9)
l.insertNode(18)
l.insertNode(11)
l.insertNode(15)
l.insertNode(1)
l.insertNode(8)
l.sortLL()
l.printLL()
l2 = linkedList()
l2.insertNode(9)
l2.insertNode(18)
l2.insertNode(11)
l2.insertNode(15)
l2.insertNode(1)
l2.insertNode(8)
l2.sortLL()
l2.printLL()
mergeTwoSortedLL(l,l2).printLL()

