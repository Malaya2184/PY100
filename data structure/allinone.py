# A single node of a singly linked list
class Node:
  def __init__(self, data, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if self.head is not None:
      current = self.head
      
      while current.next is not None:
        current = current.next

      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while current is not None:
      print(current.data, "-->", end = " ")
      current = current.next

    print("None")
# deleting first node of the singly linked list
  def deletefirstnode(self):
        if self.head is None:
          print('There is nothing to delete') 
        else:
              temp= self.head
              self.head= self.head.next

# deletion of the last node
  # def deletelastnode(self):
  #       current = self.head
  #       while current.next is not None:
  #             current = current.next
  #       current.data = current.next
        
# Singly Linked List with insertion and print methods

L = LinkedList()
L.printLL()
# deletion of a node from the linked list where there is no node
L.deletefirstnode()
L.printLL()
# insertion in to the single linked list
L.insert(3)
L.printLL()
L.insert(4)
L.printLL()
L.insert(5)
L.printLL()
# deletion of the first node from the linkedlist
L.deletefirstnode()
L.printLL()
# L.deletelastnode()
# L.printLL()