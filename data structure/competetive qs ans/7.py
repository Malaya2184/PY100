for i in range(0,5):
    for j in range(0,9):
        if(i ==0 and j == 0):
            print("*", end="")
        elif ((j%2 == 0 and j !=0) and (j > i*2+1)):
            if j == 8:
                print("*")
            else:
                print("*",end="")
        else:
            print(" ", end="")
            