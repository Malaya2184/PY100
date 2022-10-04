    def printlevlelbyUnQueue(self):
        
        if self.head is None:
            return print('there is no such linked list to print')
        else:
            levelArr = []
            levelArr.extend([self.head,None])
            
            while levelArr:
                if levelArr[0] is None:
                    return
                if levelArr[1] is None:
                    if levelArr[0].left is not None:
                        levelArr.append(levelArr[0].left)
                    if levelArr[0].right is not None:
                        levelArr.append(levelArr[0].right)
                    levelArr.append(None)
                    print(levelArr[0].data)
                    levelArr.pop(0)
                    levelArr.pop(0)
                else:
                    if levelArr[0].left is not None:
                        levelArr.append(levelArr[0].left)
                    if levelArr[0].right is not None:
                        levelArr.append(levelArr[0].right)
                    print(levelArr[0].data, end='')
                    levelArr.pop(0)