# this is the pure basics that how recurssion works and ends

def message():
    print("Heloo World")
    message1()
    print('root mesage function call is over')
def message1():
    print("Heloo World")
    message2()
    print('mesage 1 function call is over')
def message2():
    print("Heloo World")
    message3()
    print('mesage 2 function call is over')
def message3():
    print("Heloo World")
    message4()
    print('mesage 3 function call is over')
def message4():
    print("Heloo World")
    print('mesage 4 function call is over')
    
message()