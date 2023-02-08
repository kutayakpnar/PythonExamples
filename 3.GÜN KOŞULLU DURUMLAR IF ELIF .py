# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 13:33:32 2022

@author: kutay
"""


#KOŞULLU DURUMLAR IF ELIF ..............

"""a = 2 # Blok 1 'e ait kod

if (a == 2):
    print(a) # Blok 2'ye ait kod
print("Merhaba") # Blok 1 ' ait kod"""
"""
a = 2 # Blok 1 'e ait kod

if (a == 3):
    print(a) # Blok 2'ye ait kod
print("Merhaba") # Blok 1 ' ait kod

#       if (koşul): 
           # if bloğu - Koşul sağlanınca (True) çalışır. Bu hizadaki her işlem bu if bloğuna ait.
           # if bloğu - Girintiyle oluşturulur.
     #      Yapılacak İşlemler
     
yas=int(input("Lütfen yaşınızı giriniz:"))

if (yas<18):
    print("You cannot enter.")""" 

"""
sayı = int (input("Sayıyı giriniz:"))

if (sayı < 0):
    print("Negatif Sayı") """
    

#Peki if koşulu sağlanmadığında belli bir işlemin çalışmasını nasıl sağlayacağız ?
    
"""
# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")
else:
    # else bloğu -  if koşulu sağlanmazsa çalışacak.
    print("Mekana hoşgeldiniz.")
    
#else:
    print("Merhaba")
  File "<ipython-input-15-9fdf2315e01a>", line 1
    else:
       ^
SyntaxError: invalid syntax
Buradaki kod hata verdi çünkü bir else bloğu kendinden önce herhangi bir koşul bloğu yok ise çalışamaz ve Pythonda hataya yol açar.
"""

"""
if-elif-else Blokları
Önceki konumuzda koşullu durumlarımızla sadece tek bir koşulu kontrol edebiliyorduk. Ancak programlamada bir durum bir çok koşula bağlı olabilir. Örneğin bir hesap makinesi programı yazdığımızda kullanıcının girdiği işlemlere göre koşullarımızı belirleyebiliriz. Bu tür durumlar için if-elif-else kalıplarını kullanırız. Kullanımı şu şekildedir;

           if koşul: 
               Yapılacak İşlemler
           elif başka bir koşul:
               Yapılacak İşlemler
           elif başka bir koşul:
               Yapılacak İşlemler

                //
                //
           else:
               Yapılacak İşlemler """
               
#Programlarımızda, Kaç tane koşulumuz var ise o kadar elif bloğu oluşturabiliriz. Ayrıca else in yazılması zorunlu değildir. if - elif - else kalıplarında, hangi koşul sağlanırsa program o bloğu çalıştırır ve if-elif-blokları sona erer. 



























    