# Problem Statement: Suppose you have given the stock prices for respective days like (100, 180, 260, 310, 40, 535, 695). The stock price for the 1st day is 100, the 2nd day it is 180 and so on. Write a Python program to determine what days the user should buy and sell the stocks to get the maximum profit.

# In the above case, in the following scenarios user will get maximum profit.

# Buy stock on 1st day (100)
# Sell stock on 4th day (310)
# Buy stock on 5th day  (100)
# Sell stock on 7th day (695)


priceOfStock = [100, 180, 260, 310, 40, 535, 695]

i = 0
def buyStock(i,priceOfStock):
    if i < len(priceOfStock):
        for x in range(i,len(priceOfStock)):
            if priceOfStock[x]<priceOfStock[x+1]:
                print("Buy stock in day", x+1, "at price", priceOfStock[x])
                i = x+1
                if i < len(priceOfStock):
                    # print(i)
                    sellStock(i, priceOfStock)
                    break
                else:
                    break
    
def sellStock(i, priceOfStock):
    if i < len(priceOfStock):
        for x in range(i,len(priceOfStock)):
            if x == len(priceOfStock)-1:
                print("sell stock in day", x+1, "at price", priceOfStock[x])
            elif priceOfStock[x]>priceOfStock[x+1]:
                print("sell stock in day", x+1, "at price", priceOfStock[x])
                i = x+1
                if i < len(priceOfStock):
                    buyStock(i,priceOfStock)
                    break

buyStock(i,priceOfStock)
        

    
        
    
