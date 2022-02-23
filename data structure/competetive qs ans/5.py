myarr = [1,2,3,4,5,6,7,8,9]

def isunique (myarr):
    unique =0
    for i in range (len(myarr)):
        for j in range(i+1, len(myarr)):
            if(j<len(myarr)):
                if myarr[i]== myarr[j]:
                    print("array is not unique")
                    unique = 1
                    break
                else:
                    if(i == len(myarr)-2) and unique == 0:
                        print("array is unique")
                        break
                    continue  
    

isunique(myarr)