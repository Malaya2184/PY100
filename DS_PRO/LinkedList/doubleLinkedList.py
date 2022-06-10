class node :
    def __init__(self, data):
        self. data = data
        self.next = None
        self.prev = None
    
class doubleLinkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, data):
        newNode = node(data)
        
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while  current.next is not None:
                # prevNode = current
                current = current.next
            
            newNode.prev = current
            current.next = newNode
            
    def printDLL(self):
        current = self.head
        count = 0
        while current.next is not None:
            count+=1
            if count == 1:
                print("NONE<----",current.data,end="--->")
            else:
                print(current.data,end="--->")
                
            current = current.next
            
        if count ==0:
            print("NONE<----",current.data,'----> NONE')
        else:
             print(current.data,'----> NONE')
             
    def goToNode(self,data):
        current = self.head
        
        count = 1
        while current.next is not None:
            if count == data:
                print("cEntered node data :", current.data)
                print("prev node data :", current.prev.data)
                print("next node data :", current.next.data)
                break
            else:
                count+=1
                current = current.next
                 
        

l = doubleLinkedList()
l.insertNode(1)
l.insertNode(2)
l.insertNode(3)
l.insertNode(4)
l.insertNode(5)
l.insertNode(6)
l.insertNode(7)
l.insertNode(8)
l.printDLL()
l.goToNode(5)