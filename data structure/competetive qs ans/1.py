# Output Formatting: Print the number of common factors of a and b. Both the input value should be in a range of 1 to 10^12
import math
number1, number2 = map(int,input("Enter two numbers :").split())

def gcdOfTwoNumbers(number1, number2):
    if number1< 10**12+1 and number2 < 12**12+1:
        if  number1 == 0 and number2 != 0:
            return " gcd of {number1} and {number2} is :", number2
        elif  number1 != 0 and number2 == 0:
            return " gcd of {number1} and {number2} is :", number1
        else:
            return 'gcd of num1 and num2 is :', math.gcd(number1,number2)
        
print(gcdOfTwoNumbers(number1, number2))