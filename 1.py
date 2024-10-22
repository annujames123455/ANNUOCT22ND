"""
author name:annu james
program to convert celsius to fahrenheit
"""

temp=int(input("enter the temperature:"))
t=input("Is this in (C)elsius or (F)ahrenheit?")
f=0
if t=='C':
    f=9/5 * temp+32
    print(temp,"celsius is",f,"fahrenheit")
else:
    f=5/9*temp-32
    print(temp,"fahrenheit is",f,"celsius")


