# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 00:53:29 2022

@author: kutay
"""




"""#LİSTELER   KÖŞEL PARANTEZ İLE AÇILIR

a=[3,4,5,6]
b=["mehmet",3,"kutay","akpınar",28] 

# boş liste 
c = list() # it equals to c = []

# listelerde de len fonksiyonu kullanabiliriz.
liste1=[1,2,3,4,5,"kutay"]
print(len(liste1))
# string listeye dönüştürebiliriz ama her bir indeks listenin bir elemanı olur

s= "Mehmet Kutay Akpınar"
liste2 = list(s)"""

""" 
#LİSTE İNDİKSLEME VE PARÇALAMA
liste = [3,4,5,6,7,8,9,10]
a= liste[0]
b= liste[-1]
c=liste[-len(liste)]
d=liste[:2]
e= liste[3:]
f=liste[3:6]
g=liste[::2]
h =liste[::-2]"""

"""
#TEMEL LİSTE METHODLARI

liste1=[1,2,3,4,5,6]
liste2=[7,8,9,10,11,12]
#Listeler birbiri ile toplanıp tek bir liste elde edilebilinir.

liste3=liste1+liste2
print(liste3)

#listeye sadece bir tane eleman eklemek istersek?
liste=["kutay","akpınar",2001]
liste=liste +["mehmet"]
print(liste)


# LİSTENİN BİR İNDEKSİNİ DİREKT DEĞİŞTİREBİLİRİZ

liste[0]="xxxx"
print(liste)
# burada kutay elemanı xxxx olarak değişti

# Şöyle bir kullanım da mümkündür.
liste[:2] = [40,50]
liste"""

"""#LİSTELERİ TAM SAYILAR İLE DE ÇARPABİLİRİZ

liste1=[1,2,3,4,5,6]
liste1=liste1*3
print(liste1) """

#bir listeyi çarpmak demek listeyi çarpım kadar aynı listede yazdırmak demek 

#APPEND METHODU 
#APPEND FONKSİYONU İÇİNDE VERDİĞİMİZ DEĞER LİSTEYE EKLENİR

""" liste=[1,2,3,4,5,6]
liste.append(12)
print(liste)
# pop metodu
#Bu metod, içine değer vermezsek listenin son indeksindeki elemanı, değer verirsek verdiğimiz değere karşılık gelen indeksteki elemanı listeden atar ve attığı elemanı ekrana basar.
liste.pop()
print(liste)
liste.pop(2)
print(liste)"""

"""#SORT METHOU LİSTEMİZİ KÜÇÜKTEN BÜYÜĞE VE ALFABETİK OLARAK SIRALAR

liste = [34,1,56,334,23,2,3,19]
liste.sort() # Küçükten büyüğe sıralar.
print(liste)
#peki ya ben büyükten küçüğe sıralamak istiyorsam
liste2 = [34,1,56,334,23,2,3,19]
liste2.sort(reverse=True)
print(liste2)"""


"""liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = [7,8,9]

yeniliste = [liste1,liste2,liste3]
print(yeniliste)
print(yeniliste[0][2])""" 


















