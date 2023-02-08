# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:19:28 2022

@author: kutay
"""


#Programming Assignment - Basic Python Objects and Data Structures




#Problem 1
#Multiply the 3 numbers you receive from the user and print them on the screen. Try to print to the screen with the format method.

a=int(input("number one:"))
b=int(input("number two:"))
c=int(input("number three:"))
d=a*b*c
print("Multiplying numbers by each others")
print("number one:{}\nnumber two:{}\nnumber three:{}\nResult:{}".format(a,b,c,d)) 


#Problem 2
#Find the user's body mass index based on the height and weight values ​​you get from the user.

height=float(input("Please enter your height:"))
mass=float(input("Please enter your mass:"))
body_mass_index= mass / (height**2)
print("Body mass index is calculating.............")
print("Your body mass index is:{:.2f}".format(body_mass_index))


#Problem 3
# Get information about how much a vehicle has burned per kilometer and how many kilometers it has traveled, and calculate how much the driver must pay in total.

a=float(input("Please enter how much your car has burned per one kilometer:"))
b=float(input("Please enter how much km you has travelled:"))
c=a*b
print("You have to pay {:.2f} TL".format(c))

#Problem 4 
#Ask the user for two numbers and exchange their values ​​with each other.

a=int(input("Please number one:"))
b=int(input("Please number two:"))
print("Numbers are exchanging..............")
a,b=b,a
print("Number one:{}  Number two{}".format(a,b))

#Problem 5
#Take the two perpendicular sides (a, b) of a right triangle from the user and try to find the length of the hypotenuse.


a=int(input("Please enter the first perpendicular edge:"))
b=int(input("Please enter the second perpendicular edge:"))
c= ((a**2) + (b**2))**0.5
print("Hypotenuse length is:",c)







