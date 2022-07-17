
def symetricalOrpalindrom(str):
    mid = len(str)//2
    if len(str)%2 == 0:
        if str[:mid] == str[mid:]:
            print("symmetric")
        else:
            print('asymmetric')
    elif len(str)%2 == 1:
        if str[:mid]  == str[mid+1:]:
            print("symmetric")
        else:
            print('asymmetric')
        
    if str == str[::-1]:
        print('pallindrom')
    else:
        print('not a pallindrom')
    
symetricalOrpalindrom('malaya')
symetricalOrpalindrom('aabaa')