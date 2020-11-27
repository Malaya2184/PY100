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

# Singly Linked List with insertion and print methods
L = LinkedList()
L.printLL()
L.insert(3)
L.printLL()
L.insert(4)
L.printLL()
L.insert(5)
L.printLL()