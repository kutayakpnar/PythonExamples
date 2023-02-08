# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:35:57 2022

@author: kutay
"""

# DÖNGÜ YAPILARI

"a" in "merhaba"
#True
"mer" in "merhaba"
#True
"t" in "merhaba"
#False
4 in [1,2,3,4]
#True
10 in [1,2,3,4]
#False
4 in (1,2,3)
#False
""" 
#for Döngüsü
#eleman değişkeni her döngünün başında listenin,demetin vs. her bir elemanına eşit olacak ve her döngüde bu elemanla işlem yapılacak.

liste = [1,2,3,4,5,6,7]
for i in liste:
    print("Eleman:",i)

liste1 = [1,2,3,4,5,6,7]
toplam = 0
for i in liste1:
    toplam += i 
print("Toplam:",toplam)"""
"""
# Çift elemanları bastırma
liste = [1,2,3,4,5,6,7,8,9]

for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)"""
        
#Karakter Dizileri Üzerinde Gezinmek (Stringler)
        
s =  "Python"
for karakter in s:
    print(karakter) 

# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1,2),(3,4),(5,6),(7,8)]

for (i,j) in liste:
    print(i,j)
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        