# simple way to create a single linked list
class linkedlistNode:
    def __init__(self,value, nextNode=None):
        self.value= value
        self.nextNode= nextNode

# let create some node which has all the nextNode position withh null/none
# node creation = creation of instance variable of the object
node1 = linkedlistNode("5")
node2 = linkedlistNode("7")
node3 = linkedlistNode("9")
node4 = linkedlistNode("15")

# let make the linked list and reference like node1-->node2-->node3
# so that we have to assign the next node value of prev node to the next node so that it will create an reference

node1.nextNode= node2
node2.nextNode= node3
node3.nextNode= node4

# printing of the linked list
currentNode = node1
while True:
    print(currentNode.value, "-->",end=" ")
    if currentNode.nextNode is None:
        print("None")
        break
    else:
        currentNode= currentNode.nextNode