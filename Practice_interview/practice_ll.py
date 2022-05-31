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
    def printLL(self):
        if self.head == None:
            return 'there is no linkedlist created'
        else:
            current = self.head
            while current.next is not None:
                print(current.data, end='--->')
                current = current.next
            print(current.data,'--->',current.next)
            
l = linkedList()
l.insertNode(5)
l.printLL()
l.insertNode(7)
l.insertNode(8)
l.insertNode(15)
l.printLL()