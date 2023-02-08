# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:53:20 2022

@author: kutay
"""


#KULLANICIDAN INPUT ALMA

#input() fonksiyonu sayesinde yapılır

a = input("Lütfen bir sayı giriniz:") # Kullanıcıdan aldığımız değer a değişkenine eşit olacak.
print("Kullanıcının girdiği değer:",a) #bu format cinsini unutma 

"""Kullanıcının girdiği değer input fonksiyonundan string olarak bize döner.
Eğer biz bir sayı ile işlem yapacaksak kullanıcıdan aldığımız değere (stringi) float ya da int fonksiyonuyla veri tipi dönüştürme işlemi yapmamız gerekir
Eğer biz bir sayı ile işlem yapacaksak kullanıcıdan aldığımız değere (stringi) float ya da int fonksiyonuyla veri tipi dönüştürme işlemi yapmamız gerekir. Çünkü aşağıdaki gibi bir program yanlış çalışacaktır.

# Hatalı Çalışma
a = input("Lütfen bir sayı giriniz:")
print(a * 3) # Girdiğimiz değer 5 ise sonucu 15 bekleriz. Ancak sonuç 555 şeklinde ortaya çıkar.
Lütfen bir sayı giriniz:5
555
# Doğru Çalışma
a = int(input("Lütfen bir sayı giriniz:")) # Veri tipi dönüşümü
print(a * 3) 
Lütfen bir sayı giriniz:5
15""" 
