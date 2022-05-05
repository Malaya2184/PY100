#  simple way to understand linked list

#  to create a single node object inside a linkedlist object



from itertools import count
from locale import currency


class node :
    def __init__(self, data, next= None):
        self.data = data
        self.next = next
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insertnode(self, data):
        newNode = node(data)
        
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                
            current.next = newNode
            
    def printLinkedList(self):
        current = self.head
        
        if current is not None:
            while current is not None:
                print(current.data,"----->", end="")
                current = current.next
            print("none")
        else:
            print("there is no linked list")
    
    def deletefirstnode(self):
        if self.head is not None:
            current = self.head
            self.head = current.next
        else:
            print("there is nothing to delete in the linkedlist")
            
    def deletelastnode(self):
        current = self.head
        while current.next is not None:
            prev = current
            current = current.next


        prev.next = None
        
    def searchnode(self,num):
        count = 1
        current = self.head
        
        while current is not None:
            if current.data == num:
                break
            current = current.next
            count+=1
            
        if current == None:
            print("no such number is there")
        else:
            print("found at the ",count," posithion")
            
    # def deleteAnynode(self, num):
    #     current = self.head
    #     if(current==None):
    #         print("there is nothing to delete")
    #         return
    #     while current is not None :
    #         if current.next is None and current.data ==num:
    #             self.deletelastnode()
    #         current = current.next
    def sortlinkedlist(self):
        current = self.head
        linkedlist= []
        if self.head is not None:
            while current is not None:
                linkedlist.append(current.data)
                current=current.next
            
            
            linkedlist.sort()
            
            self.head = None
            for i in  linkedlist:
                self.insertnode(i)
    
    def lenoflinkedlist(self):
        current = self.head
        count = 0
        while current is not None:
            count+=1
            current=current.next
            
        return count+1
    
    # TODO: little mistake and find it out.
    def insertElemAtPos(self,num,pos):
        current = self.head
        
        if current is not None and pos<=self.lenoflinkedlist():
            if pos == self.lenoflinkedlist():
                self.insertnode(num)
            else:
             
                count =0
                while current is not None:
                    prev = current
                    count+=1
                    current = current.next
                    
                    if(count == pos):
                     
                        addNode=node(num)

                        prev.next  = addNode
                        addNode.next = current
                       
                        break
        
        
        
        
        
                
l = linkedlist()
l.insertnode(5)
l.insertnode(6)
l.printLinkedList()
l.insertnode(1)
l.printLinkedList()
l.deletefirstnode()
l.insertnode(17)
l.printLinkedList()
l.searchnode(17)
l.deletelastnode()
l.searchnode(1)
l.searchnode(17)
l.insertnode(66)
l.insertnode(3)
l.insertnode(2)
l.insertnode(99)
l.printLinkedList()
l.sortlinkedlist()
l.printLinkedList()
l.insertElemAtPos(101,7)
l.insertElemAtPos(103,5)
l.printLinkedList()
# l.deleteAnynode(66)
# l.printLinkedList()
