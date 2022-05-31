from requests import delete


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
            return 'there is no linkedlist created'
        else:
            current = self.head
            while current.next is not None:
                print(current.data, end='--->')
                current = current.next
            print(current.data,'--->',current.next)
    def deleteLastNode(self):
        current = self.head
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
l = linkedList()
l.insertNode(5)
l.printLL()
l.insertMultipleNode([7,8,15])
l.printLL()
l.deleteLastNode()
l.printLL()