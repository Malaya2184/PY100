class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class linkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, data):
        newNode = node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            
    def insertMultipleNode(self, arr):
        for i in arr:
            self.insertNode(i)
            
    def printLL(self):
        if self.head == None:
            return print('there is no linkedlist created')
        else:
            current = self.head
            while current.next is not None:
                print(current.data, end='--->')
                current = current.next
            print(current.data,'--->',current.next)
            
    def deleteLastNode(self):
        if self.head is None:
            return(print("no linkedlist present"))
        elif self.head.next is None:
            self.head = None
            return(print('there was a single node in LL which has deleted'))
        else:
            current = self.head
            while current.next is not None:
                prev = current
                current = current.next
            prev.next = None
            
    def deleteFirstNode(self):
        if self.head is None:
            return(print("no linkedlist present"))
        elif self.head.next is None:
            self.head = None
            return(print('there was a single node in LL which has deleted'))
        else:
            current = self.head
            if current.next is not None:
                self.head = current.next
                
    def lengthOfLL(self):
        current = self.head
        count = 0
        if  current is None:
            return 'linked list has nt created yet unable to find length'
        else:
            while current.next is not None:
                count+=1
                current = current.next
            return(print('length of linked list is :', count+1))
        
    def sortLinkedListUsingArray(self):
 
        current = self.head
        myarr = []
        while current.next is not None:
            myarr.append(current.data)
            current = current.next
        myarr.append(current.data)
        myarr.sort()
        self.head= None
        self.insertMultipleNode(myarr)
        
    def reverseLL(self):
        current = self.head
        prev = None
        while current.next is not None:
            right = current.next
            current.next = prev
            prev = current
            current = right
        current.next = prev
        self.head = current
        
    def printMiddleOfLL(self):
        singleStep = self.head
        doubleStep = self.head
        
        while doubleStep is not None and doubleStep.next is not  None:
            singleStep = singleStep.next
            doubleStep = doubleStep. next.next
        
        return(singleStep.data)
    def deleteMidOfLL(self):
        singleStep = self.head
        doubleStep = self.head
        
        while doubleStep is not None and doubleStep.next is not  None:
            prev = singleStep
            singleStep = singleStep.next
            doubleStep = doubleStep.next.next
        
        prev.next = singleStep.next
        
        
# function outside the class
def mergeTwoSortedLL(l, l2):
    
    current1 = l.head
    current2 = l2.head
    l3 = linkedList()
    
    while current1 is not None and current2 is not None:
        
        if current1.data < current2.data:
            l3.insertNode(current1.data)
            current1 = current1.next
        else:
            l3.insertNode(current2.data)
            current2 = current2.next
            
    if current1 is None:
        
        while current2.next is not None:
            l3.insertNode(current2.data)
            current2 = current2.next
        l3.insertNode(current2.data)
    else:
        while current1.next is not None:
            l3.insertNode(current1.data)
            current1 = current1.next
        l3.insertNode(current1.data)
        
    return l3
            
        
            
l = linkedList()
l.insertNode(5)
l.deleteLastNode()
l.printLL()
l.insertMultipleNode([7,8,15])
l.printLL()
l.deleteLastNode()
l.printLL()
l.lengthOfLL()
l.deleteFirstNode()
l.printLL()
l.lengthOfLL()
l.insertMultipleNode([25,3,5])
l.printLL()
l.lengthOfLL()
l.sortLinkedListUsingArray()
l.printLL()
l.lengthOfLL()
l.reverseLL()
l.insertNode(1)
l.printLL()
print(l.printMiddleOfLL())
l.deleteMidOfLL()
l.printLL()
l.sortLinkedListUsingArray()
l.printLL()
l2 = linkedList()
l2.insertNode(9)
l2.insertNode(18)
l2.insertNode(11)
l2.insertNode(15)
l2.insertNode(1)
l2.insertNode(8)
l2.sortLinkedListUsingArray()
l2.printLL()
mergeTwoSortedLL(l,l2).printLL()