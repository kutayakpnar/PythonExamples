# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:40:36 2022

@author: kutay
"""



a=input("Please enter shape:")
if (a=="rectangular"):
    e1=int(input("Please enter length od edge1:"))
    e2=int(input("Please enter length od edge2:"))
    e3=int(input("Please enter length od edge3:"))
    e4=int(input("Please enter length od edge4:"))
    if (e1==e2 and e3==e4 and e1==e3):
        print("It is a square.")
    elif(e1==e3 and e2==e4):
        print("It is a rectangular.")
    else:
        print("It isquadrilateral.")
elif (a=="triangular"):
    e1=int(input("Please enter length od edge1:"))
    e2=int(input("Please enter length od edge2:"))
    e3=int(input("Please enter length od edge3:"))
    if (abs(e1+e2)> e3 and abs(e1+e3)>=e2 and abs(e3+e2)>e1):
        if(e1==e2 and e1==e3):
            print("It is equiletarel triangle")
        elif((e1==e2 and e1!=e3) or (e2==e3 and e2!=e1) or (e1==e3 and e3!=e2)):
            print("It isosceles triangle")
        else:
            print("It is scalene triangle")
        
        

        
    else:
        print("It does not define a triangular.")

else:
    print("Please enter rectangular or triangular!")   
    