# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:36:11 2022

@author: kutay
"""


#DICTIONARIES
# HER BİR DEĞER BİR KEYDİR KEYİN KARŞISINDAKİ DEĞER VALUEDUR.

# Süslü Parantez ve iki nokta (:) ile anahtar değerlerimizi yerleştirelim.
sözlük1 = {"sıfır":0,"bir":1,"iki":2,"üç":3}
sözlük2=dict()

a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}


print(sözlük1["sıfır"]) #her bir keye gelen valu değerini böylece yazdırabiliriz.

print(a["iki"])
print(a["iki"][1][0])
print(a["üç"])
a["üç"] +=15 
print(a)

#Bir sözlüğe dinamik olarak da eleman ekleyebiliriz.

# Sözlük oluşturalım.
b = {"bir":1,"iki":2,"üç":3}
b["dört"] = 4 
print(b)

"""İç içe Sözlükler
Tıpkı listeler gibi, iç içe sözlükler de oluşturulabilir."""

# İç içe sözlük

a = {"sayılar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}}
x=a["sayılar"]["bir"]

y=a["meyveler"]["kiraz"]


#TEMEL SÖZLÜK METHODLARI

yeni_sözlük = {"bir":1,"iki":2,"üç":3}

print(yeni_sözlük.values())
print(yeni_sözlük.keys())
print(yeni_sözlük.items())




































