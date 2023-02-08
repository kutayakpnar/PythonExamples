# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:38:41 2022

@author: kutay
"""

"""
CALCULATING GRADE
"""

mt1 = int(input("Midterm1:"))
mt2 = int(input("Midterm2:"))
final = int(input("Final:"))


genel_not=  mt1 * 3/10 + mt2 * 3/10 + final * 4/10

if (genel_not >= 90):
    print("AA")
elif (genel_not >= 85):
    print("BA")
elif (genel_not >= 80):
    print("BB")
elif (genel_not >= 75):
    print("CB")
elif (genel_not >= 70):
    print("CC")
elif (genel_not >= 65):
    print("DC")
elif (genel_not >= 60):
    print("DD")
elif (genel_not >= 55):
    print("FD")
else:
    print("FF")