# 1. Write a program to check if the entered number is palindrome or not.
# Take input from user. Check all validation.

number=int(input("Enter number:"))
temp=number
revers=0
while(number>0):
    dig=number%10
    revers=revers*10+dig
    number=number//10
print("The number is a palindrome") if temp==revers else print("The number isn't a palindrome")