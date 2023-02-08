# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:12:01 2022

@author: kutay
"""


#While döngüleri
#while döngüsü girintilerle oluşur while döngüsü true oldukça döngü çalışır....

#while döngüleri belli bir koşul sağlandığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder. while döngülerinin sona ermesi için koşul durumunun bir süre sonra False olması gereklidir.Yapısı şu şekildedir;

""" #                       while (koşul):
                                İşlem1
                                İşlem2
                                İşlem3
                                  //
                                  // """
                                  
                                  
"""i= 0 
while (i <= 10):
    print(i)
    i += 1"""
    
"""a=len(liste)
index = 0
while(index<a):
    print("index:",index,"eleman:",liste[index])
    index += 1"""
    
"""
# range fonksiyonu
    
liste = list(range(0,20)) # list fonksiyonuyla listeye dönüştürebilir.
print(liste)

print(*range(15)) # Başlangıç değeri vermediğimiz 0'dan başlar 
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
print(*range(5,20,2)) # 5'ten 20'ye kadar olan sayıları 2 atlayarak oluşturur.
#5 7 9 11 13 15 17 19
print(*range(5,100,5)) # 5'ten 100'e kadar olan ve 5 ile bölünebilen sayılar
#5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95

print(*range(20,0)) # 20'den geri gelen sayıları oluşturmaz.
print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.
#20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for sayı in range(0,10):
    print(sayı)"""
    
i = 0 # break kullanmaya çalışalım.

while (i < 20):
    print(i)
    if (i == 10):
        break # i'nin değeri 10 olunca bu koşul sağlanıyor ve  break ifadesiyle karşılaşıldığı için döngü anında sona eriyor.
    i +=1

# while True kullanılırsa break çalışmadıkça bu döngü sonsuza kadar çalışır demek.
    
while True:
    isim=input("lütfen isim giriniz.Çıkmak için q ya basın")
    if (isim == "q"):
        break
    print(isim)

#Continue ifadesi
    
#continue ifadesi break'e göre biraz daha az kullanılan bir ifadedir. Anlamı şu şekildedir;

    #Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini
    #yapmadan direk bloğunun başına döner    
    
liste = [1,2,3,4,5,6,7,8,9] # continue kullanalım.


for i in liste:
    if (i == 3 or i == 5):
        continue
    print("i:",i)  
    
 #continuenun altında kalanlar
 yapılmaz
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


