
def check(str):
    flag1 = False
    flag2= False
    for i in str:
        # to check that the charcter is string or not
        if i.isalpha():
            flag1= True
        # to check that the charcter is number or not
        if i.isdigit():
            flag2 = True
        if flag1 and flag2 is True:
            break
            
    return flag1 and flag2

print(check('welcome2.5home'))