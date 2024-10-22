"""
author name:annu james
program to find the largest of three numbers
"""


num1=int(input("enter the number1"))
num2=int(input("enter the number 2"))
num3=int(input("enter the number 3"))
if(num1>num2 and num1>num3):
    print("largest=num1")
elif(num2>num3 and num2>num3):
    print("largest=num2")
else:
    print("num 3 is the largest")

