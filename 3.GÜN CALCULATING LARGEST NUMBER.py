# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:32:04 2022

@author: kutay
"""


"""
**********CALCULATING LARGEST NUMBER
**********
"""

a=int(input("Please enter the number:"))
b=int(input("Please enter the number:"))
c=int(input("Please enter the number:"))

if(a>=b and a>=c):
    print("The largest number:",a)
elif(b>=a and b>=c):
    print("The largest number:",b)
elif(c>=a and c>=b):
    print("The largest number:",c)
    

    

