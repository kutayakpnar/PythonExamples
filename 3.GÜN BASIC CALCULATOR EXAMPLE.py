# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:02:35 2022

@author: kutay
"""


# BASIC CALCULATOR EXAMPLE 

print(""" 
     

****************CALCULATOR*****************

Mathematical Operations:
1.Summation
2.Subtract
3.Multiplication
4.Division
  """) 
    
a= int(input("Please enter the first number:"))
b= int(input("Please enter the second number:"))
operation=input("Please enter operation you want:")

if (operation=="1"):
    print(a+b)
elif (operation == "2"):
    print(a-b)
elif (operation == "3"):
    print(a*b)
elif(operation == "4"):
    print(a/b)
else:
    print("Please enter a valid operation")
    
    
