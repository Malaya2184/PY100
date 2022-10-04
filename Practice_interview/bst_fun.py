class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    
    def __init__(self):
        self.head = None
        
    def insertNode(self, data):
        
        newnode = node(data)
        
        if self.head is None:
            self.head = newnode
        else:
             current = self.head
             
             while current is not None:
                 
                 if data > current.data:
                     if current.right is None:
                         current.right = newnode
                         break
                     else:
                         current = current.right
                 else:
                     if current.left is None:
                         current.left =newnode
                         break
                         
                     else:
                         current = current.left
                         
                         
# printing all element of the bst
    def printBst(self,head):
        
        current = head
        if current == self.head:
            print(current.data)
        elif head is None:
            return

        if current.left is not None or current.right is not None:
            if current.left is not None:
                print(current.left.data)
            if current.right is not None:
                print(current.right.data)
            
        left = self.printBst(current.left)
        right = self.printBst(current.right)
    

    
    # for this you have to understand the piece of the code
    
    # arr = [1]

    # if arr:
    #     print(True)
    # else:
    #     print(False)
    # if the arr will empty then it will return false 
    # ====================================================
    
    # print level by level in bst
    def printBstLevelByLevel(self):
        
        current = self.head
        levelQ = []
        
        if self.head is None:
            return print("there is no binary tree present")
        else:
            levelQ.append(current)
            
            while levelQ:
                
                length = len(levelQ)
                
                while length > 0:
                    
                    current = levelQ.pop(0)
                    print(current.data,end=' ')
                    if current.left is not None:
                        levelQ.append(current.left)
                    if current.right is not None:
                        levelQ.append(current.right)
                        
                    length -= 1
                print()
                    
    # print level by level in bst by using unquing null / none yepee done
    # for extended function refer to bstLevelPrintExtended.py
    def printlevlelbyUnQueue(self):
        
        if self.head is None:
            return print('there is no such linked list to print')
        else:
            levelArr = []
            levelArr.extend([self.head,None])
            while levelArr:
                if levelArr[0] is None:
                    return
                if levelArr[0].left is not None:
                    levelArr.append(levelArr[0].left)
                if levelArr[0].right is not None:
                    levelArr.append(levelArr[0].right)
                         
                if levelArr[1] is None:
                    levelArr.append(None)
                    print(levelArr[0].data)
                    levelArr.pop(0)
                    levelArr.pop(0)
                else:
                    print(levelArr[0].data, end=' ')
                    levelArr.pop(0)
    
    # print left  view of a binary tree
    def printLeftView(self):

        if self.head is None:
            return print('there is no binary tree')
        else:
            current = self.head
            
            while current.left is not None:
                print(current.data)
                current = current.left
            print(current.data)
               

        
        
b = BinarySearchTree()
b.insertNode(5)
b.insertNode(3)
b.insertNode(7)
b.insertNode(2)
b.insertNode(4)
b.insertNode(6)
b.insertNode(8)
b.insertNode(9)
b.insertNode(1)
b.insertNode(10)
print(b.head.data)
b.printBst(b.head)
print('==========LEVEL BY LEVEL PRINTING OF THE BST ==========')
b.printBstLevelByLevel()
print('==========LEVEL BY LEVEL PRINTING OF THE BST by unquew null / none ==========')
b.printlevlelbyUnQueue()
print('==========PRINT LEFFT VIEW OF THE BINARY TREE ==========')
b.printLeftView()

            
                     
                     
            