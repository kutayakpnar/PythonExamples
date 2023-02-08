# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:24:15 2022

@author: kutay
"""


"""
*******************CALCULATING BODY MASS INDEX***************
"""

mass=float(input("Please enter your mass:"))
height=float(input("Please enter your height:"))
bmi= mass /(height*height)
if (bmi<=18.5):
    print("You are weak.")
elif(18.5<bmi<=25):
    print("You are normal.")
elif(25<bmi<=30):
    print("You are overweight.")
elif(30<bmi):
    print("You are obese.")
else:
    print("There is an error.Please enter values again.")
    