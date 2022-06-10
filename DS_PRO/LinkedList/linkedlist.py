
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
        
    def insertmultipleNodes(self,arr):
        for i in arr:
            self.insertnode(i)
            
    def deleteLastNode(self):
        current=self.head
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
        
    def sortLinkedList(self):
        current = self.head
        arr=[]
        while  current is not  None:
            arr.append(current.data)
            current=current.next
        
        arr.sort()
        self.head = None
        self.insertmultipleNodes(arr)
    
    def deleteFirstNode(self):
        current = self.head
        
        if current.next == None:
            self.head = None
        else:
            self.head = current.next
            
    def searchElementInLinkedlist(self,data):
        current = self.head
        count = 1
        while current is not None:
            if current.data == data:
                print(data, " first found at", count, "position")
                break
            else:
                current = current.next
                count+=1

l = linkedList()
l.insertnode(5)
l.printLinkedList()
l.insertnode(9)
l.printLinkedList()
l.insertmultipleNodes([3,5,7,9,10])
l.printLinkedList()
l.deleteLastNode()
l.printLinkedList()
l.sortLinkedList()
l.printLinkedList()
l.deleteFirstNode()
l.printLinkedList()
l.searchElementInLinkedlist(9)
l.searchElementInLinkedlist(7)
l.searchElementInLinkedlist(5)