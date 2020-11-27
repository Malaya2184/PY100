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
  def deletelastnode(self):
        current = self.head
        while current.next is not None:
              previous = current
              current = current.next
        previous.next = None
# searching of an element in the linked list
  def searchnode(self, value):
    self.value = value
    if self.head is None:
          print("There is nothing to search in this linked list")
    else:
          current = self.head
          while current.data != value:
                if current.next is None:
                      print("opps not found, better luck next time")
                      break
                else:
                      current= current.next
          if current.data == value:
                print("yepee found it")
# counting the number of nodes
  def countnodes(self):
        current= self.head
        count = 0
        if self.head is not None:
          while current.next is not None:
                count += 1
                current= current.next
        else:
              return 0
        return count+1
# sorting of element in the linked list
  def sortlinkedlist(self):
        current = self.head
        LinkedListList = []
        if current is not None:
          while current is not None:
                LinkedListList.append(current.data)
                current= current.next
          print(LinkedListList)
          LinkedListList.sort()
          print(LinkedListList)
        else:
              print("There is nothing to sort")

        
# Singly Linked List with insertion and print methods

L = LinkedList()
L.printLL()
# counting the number of nodes when there is no nodes
print("there are ",L.countnodes(),"number of nodes in this linked list")
# searching of a node when there is no node
L.searchnode(4)
# deletion of a node from the linked list where there is no node
L.deletefirstnode()
# sorting of linked list when therwe is no node
L.sortlinkedlist()
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
# deletion of last node
L.deletelastnode()
L.printLL()
# searching of a node in the linked list
L.searchnode(15)
L.insert(15)
# searching of the node
L.searchnode(15)
L.printLL()
# counting the number of nodes in tghe linked list
print("there are ",L.countnodes(),"number of nodes in this linked list")
# inserted anathor element
L.insert(2)
# sorting of linlkedlist
L.sortlinkedlist()