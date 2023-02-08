# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:23:10 2022

@author: kutay
"""


print("""
************ BASIC USER LOGIN SYSTEM ******************
""")

sys_nickname="Kutay"
sys_password="1234"

nickname=input("Please enter the nickname:")
password=input("Please enter the password:")

if (sys_nickname==nickname and sys_password== password ):
    print("You have successfully logged into the system")
elif(sys_nickname==nickname and sys_password!=password ):
    print("Your password or nickname is wrong.Please try again." )
elif(sys_nickname!=nickname and sys_password==password ):
    print("Your password or nickname is wrong.Please try again." )
elif(sys_nickname!=nickname and sys_password!=password ):
    print("Your password or nickname is wrong.Please try again." )
    
    


