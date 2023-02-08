# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:57:30 2022

@author: kutay
"""

#BASIC PLAYER REGISTRATION PROGRAM  

x=list()
player_name=input("Please enter player's name:")
player_surname=input("Please enter player's surname:")
player_team=input("Please enter player's surname:")
x.append(player_name)
x.append(player_surname)
x.append(player_team)
print("Please wait.............")
print("PLAYER NAME:{}\nPLAYER SURNAME:{}\nPLAYER'S TEAM:{}".format(x[0],x[1],x[2]))

#or we can coding like below

x=list()
player_name=input("Please enter player's name:")
player_surname=input("Please enter player's surname:")
player_team=input("Please enter player's surname:")
x=[player_name,player_surname,player_team]
print("Please wait.............")
print("PLAYER NAME:{}\nPLAYER SURNAME:{}\nPLAYER'S TEAM:{}".format(x[0],x[1],x[2]))
