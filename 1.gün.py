# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:43:04 2022

@author: kutay akpınar""
"""

""" a=10
b=20 

a,b = b,a
print(a)
print(b)

#iki değişkeni birbiriyle değiştirme 


c=10
c *=5
print(c)""" 

""" a=10
b=15 

c=a+b 
print(c)

x = 10 
y = 2 
print(x/y)  # tek / olunca sonucu float olarak bastırdı tam sayı bölmesi yapmak için // kullanman lazm 

k = 15
l= 4

i= k //l  # sonuç 3 çıktı yani en yakın tam sayıya yuvarladı""" 

# % işareti iki sayı arasından bölümün kalanını bulmaya yarar.

"""a = 15 
b = 4 
c = a%b
print(c) 

# ** iki kere çarpı işareti üs bulmaya yarar

x = 2
y = 3 

z = x ** y
print(z)

l = -a 
print(l)"""


"""a = "mehmet kutay akpınar"
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])

print(a[2:])
print(a[:6])

print(a[4:12])
print(a[::2])

print(len(a))"""

# Stringlerin indekslerini değiştiremeyiz ama stringleri birbirleri ile toplayabiliriz

"""a = "mehmet "
b= "kutay "
c = a+b

print(c)

x = "kutay "
x=x*3"""

"""a = 43
a = float(a)

b = 4.7
b = int(b)             İNTEGERI FLOATA FLOATI İNTEGERA ÇEVİREBİLİRİZ"""

# sayıları stringe çevirebiliriz ama stringleri sayılara çeviriken ondalık tabanda yazılması gerekir

""" a=45
a = str(a)
c=len(a)

b= "258484848"
b = int(b)

# aynı zamanda stringleri ondalık sayılara da çevirebiliriz ama yine ondalık tabanda olması lazım


x = "123.789"
x = float(x) """

#------------------------------------------------------------------------------------------------------------

#PRINT" FONKSIYONU VE FORMATLAMA#

"""
    "" print("kutay")
     # fakat biz print fonksiyonu ile birçok değeri aynı anda bastırabiliriz sadece araya virgül koymamız gerek """
     
"""print("mehmet",22,"kutay") 
     
    # STRINGLERDEKİ KISAYOLLAR 
    
    # \n KARAKTERİNDEN SONRA GELEN İNDEKSLER ALT SATIRA YAZDIRILIR MESELA :
    
    print("mehmet\nkutay\nakpınar")
    
    # \t karakterinden sonra iki indeks arası bir tab kadar boşluk bırakılır
    
    print("mehmet\tkutay")
    
    #type() fonksiyonu bizim veri tipimzi söyler float int str vb....
    
    # sep parametresi değerleri birbirinden ayırmamızı sağlar 
    
    print(34,56,78,45,sep=" ")
    
    print(34,56,78,45,sep="/")"""
    
    #Yıldızlı Parametreler
 #Eğer bir stringin başına * işareti koyup, print fonksiyonuna gönderirsek bu string karakterlerine ayrılacak ve her bir karakter ayrı birer string olarak davranılarak ekrana basılacaktır."""
    
"""    print(*"mehmet kutay akpınar")
    
    print(*"TBMM",sep=(",,"))"""
    


# FORMATLAMA 

print("Benim adım {} {}".format("kutay","akpınar"))
print("benim yaşım {}".format(22))

a = 10 
b = 20

print("{} ile {} çarpımı {}'dır".format(a,b,a*b))

# Süslü parantezlerin içindeki sayılar format fonksiyonun içinden hangi sıradaki değerin geleceğini söylüyor.4

print("Benim adım {2} {0} {1}".format("kutay","akpınar","mehmet"))

# Süslü parantezlerin içindeki kullanım ondalıklı kısmın sadece 2 basamağına kadar almak istediğimiz söylüyor.
print("{:.2f} {:.2f} {:.3f}".format(3.1463,5.324,7.324324))









    




