# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:16:46 2022

@author: kutay
"""

#lıst comprehension

# liste1'den liste2'yi oluşturalım.

""" liste1 = [1,2,3,4,5]

liste2 = list() # veya liste2 = [] ikisi de boş liste oluşturur.


for i in liste1:
    liste2.append(i) # liste2 'ye liste1 in elemanları for döngüsü yardımıyla atıyoruz.
    
print(liste2)
[1, 2, 3, 4, 5]"""

#Bunu şu şekilde de yapabiliriz..

"""
liste1 = [1,2,3,4,5] # Örnek 1 

liste2 = [i for i in liste1] # List Comprehension

print(liste2)

liste3=[2,4,6,8]
liste4=[i**2 for i in liste3]
print(liste4)

liste5=[(1,2),(3,4),(5,6)]
liste6=[(i*2,j*2) for (i,j) in liste5]
print(liste6)

liste1 = [1,2,3,4,5,6,7,8,9,10] # Örnek 4

liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension

print(liste2) # yani i04 ve i=9 u bastırmadı"""

"""
liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = list()
for i in liste:
    print(i) ## Buradaki i değeri de aslında bir liste.

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = list()
for i in liste:
    for x in i:
        print("x:",x)
        liste2.append(x)
print(liste2)"""

# List Comprehension 

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = [x for i in liste for x in i] # Biraz karmaşık
print(liste2)

    











