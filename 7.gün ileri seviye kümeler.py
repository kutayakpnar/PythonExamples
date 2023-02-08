#İleri Seviye Kümeler (Sets)
#Bu konuda yeni bir veritipi olan kümeler veya ingilizce adıyla setleri öğreneceğiz.

x =  set() # Boş küme

liste = [1,2,3,3,1,1,2,2,2] # Aynı elemanı birçok defa  barındıran bir liste
x = set(liste) # Veri tipi dönüşümü
x # Aynı elemanlar tek bir elemana indirgendi.
print(x) #{1, 2, 3}
y=set("Python Programlama Dili")
print(y) # {'l', ' ', 'o', 'a', 'g', 'm', 'D', 'i', 'P', 'h', 'r', 't', 'n', 'y'}

#kümeler süslü parantez ile yazılır ve eğer bir elemandan 2 tane varsa bile sadece bir kere yazılır.
x = {"Python","Php","Python"}
print(x) # Aynı elemanlar teke indirgendi.
#{'Php', 'Python'}

#For döngüsüyle Gezinmek
#Kümeler de tıpkı sözlükler gibi sırasız bir veri tipidir. Bunu for döngüsüyle görebiliriz.

x = {"Python","Php","Java","C","Javascript"}
for i in x:
    print(i) #Java
#Javascript
#Php
#Python
#C


#Peki bir kümenin elemanlarına direk olarak ulaşabiliyor muyuz ?

#x
#{'C', 'Java', 'Javascript', 'Php', 'Python'}
# x[0] hata verir.

#pki küme elemanlarına ulaşırız.Kümeyi listeye çeviriz.

liste = list({1,2,3,4,5})

liste[0]
#1

#kümelerin methodları:

#Kümelerin Metodları
#Eleman Eklemek : add() metodu
#Kümeye eleman eklemimizi sağlar. Aynı eleman eklenmeye çalışırsa hata vermez ve herhangi bir ekleme işlemi yapmaz.

x = {1,2,3}
x.add(4)
print(x) #{1, 2, 3, 4}
x.add(3)
print(x) #{1, 2, 3, 4}

#İki kümenin farkı : difference() metodu
#Bu metod birinci kümenin ikinci kümeden farkını döner.

    #küme1.difference(küme2) # Küme1'in Küme2'den farkı


küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
a=küme1.difference(küme2)
print(a)#{3,10,100,-2}
küme2.difference(küme1)
#{-1, 23}
print(küme1)    #{1, 2, 3, 100, 34, 10, -2}
                #{1, 2, 34, 23, -1}         ikisi de aynı kaöış peki farklarını bulup diğer kümeye atamak istersem napıcam?
print(küme2)


#İki kümenin farkı ve güncelleme : difference_update() metodu
#Bu metod birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.

#küme1.difference_update(küme2) # Küme1'in Küme2'den farkı
küme1={-2, 1, 2, 3, 10, 34, 100}
küme2={-1, 1, 2, 23, 34}
küme1.difference_update(küme2)
print(küme1) # Farka göre güncellendi.
#{-2, 3, 10, 100} #sadece farkları küme1 oldu

#Kümeden Eleman Çıkartmak : discard() metodu
#İçine verilen değeri kümeden çıkartır. Eğer kümede öyle bir değer yoksa, bu metod hiçbir şey yapmaz(Hata vermez).
a={1,2,3,4,6} #{1, 3, 4, 5, 6}
a.discard(2)
a.discard(100)

#Küme kesişimleri : intersection() metodu
#Bu metod iki kümenin kesişimleri bulmamızı sağlar.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
x=küme1.intersection(küme2)
print(x) #{1, 2, 34}
y=küme1.intersection_update(küme2)
print(küme1) #{1, 2, 34}

#
#Kümeler ayrık küme mi ? : isdisjoint() metodu
#Bu metod, eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme3 = {30,40,50}
küme1.isdisjoint(küme2)
#False
küme1.isdisjoint(küme3)
#True


#Alt kümesi mi ? : issubset() metodu
#Bu metod , birinci küme ikinci kümenin alt kümesiyse True, değilse False döner.

küme1 = {1,2,3}
küme2 = {1,2,3,4}
küme3 = {5,6,7}
küme1.issubset(küme2)
#True
küme1.issubset(küme3)
#False

#Birleşim Kümesi : union() metodu
#Bu metod, iki kümenin birleşim kümesini döner.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.union(küme2)
#{-2, -1, 1, 2, 3, 10, 23, 34, 100}

#Birleşim Kümesi ve update : update() metodu
#Bu birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.update(küme2)
küme1