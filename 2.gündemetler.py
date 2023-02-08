# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:29:40 2022

@author: kutay
"""


# DEMETLER(TUPLES), LİSTELERE BENZERLER AMA LİSTELERDEN EN ÖNEMLİ FARKI DEĞİŞTİRİLEMEZ OLUŞUSUR.

# Demet elemanları parantez içine alınarak demet oluşturulabilir.
demet = (1,2,3,4,5,6,7,8,9)
print(demet[0])
print(demet[4])

# Demeti oluşturalım.
demet = (1,2,3,"Mustafa","Murat","Coşkun")
# "Mustafa" elemanının indeksini buluyoruz.
print(demet.index("Mustafa") )

#count metoduyla içine verdiğimiz değerin demette kaç defa geçtiğini bulabiliriz.

demet3 = (1,23,34,34,2,1,4,5,1,1,34)
print(demet3.count(1))
