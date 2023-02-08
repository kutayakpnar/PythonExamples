""" 
#METODLAR
#Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objelere özgü fonksiyonlardır ve objelerin üzerinde metodlar şu şekilde kullanılır.
#obje.herhangi_bir_metod(değerler(opsiyonel))

liste=[1,2,3,4,5,6]
liste.insert(1,"Kutay") #listenin 1. indeksine kutay ekleyecek
#print(liste) #[1, 'Kutay', 2, 3, 4, 5, 6]
liste.pop() #listenin son elemanını atar
print(liste) #[1, 'Kutay', 2, 3, 4, 5]# """ #birçok metod var araştıra araştıra öğrenirsin

#fonkdiyonlar ve fonksiyonların kullanılması
""" Fonksiyon tanımlamanın yapısı şu şekildedir;

        def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
            # Fonksiyon bloğu
            Yapılacak işlemler
            # dönüş değeri - Opsiyonel """

"""def selamla():
    print("Merhaba Arkadaşlar")

#type(selamla) # Fonksiyonumuz tanımlandı.
                         #function
selamla()
#Peki fonksiyonumuzun içine bir tane değer verseydik ne olurdu ?
#selamla("python") # Hata verdi çünkü fonksiyonumuz hiçbir değer almıyor."""

#Şimdi fonksiyonun içine parametre vererek yazmayı deneyelim.

"""def selamla(isim):
    print("merhaba",isim)

selamla("kutay")

#!!!!!!!!!!Bizim fonksiyon tanımlarken tanımladığımız herbir değişken birer Parametre , fonksiyon çağrısı yaptığımız zaman içine gönderdiğimiz değerler ise Argüman olmaktadır.

#Toplama Fonksiyonu yazalım"""
"""
def toplama(a,b,c):
    print("Toplamları:",a+b+c)

toplama(5,15,10)

#faktöriyel fonksiyou

def fakto(sayı):
    total=1
    if (sayı == 0 or sayı ==1):
        print("Faktoriyel:",total)
    else:
        while(sayı > 1):
            total=total*sayı
            sayı-=1
        print("Faktoriyel:", total)

fakto(5)"""
#FONKSİYONARDA RETURN İFADESİ

#return ifadesi fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesi anlamı taşır. Böylelikle, fonksiyonda aldığımız değeri bir değişkende depolayabilir ve değeri programın başka yerlerinde kullanabiliriz.
#Şimdi iki tane çok basit fonksiyon yazalım ve return neden gereklidir anlamaya çalışalım.

"""
def toplama(a,b,c):
    return a+b+c
def ikiylecarp(x):
    return x*2

print(ikiylecarp(toplama(1,2,3)))  # return yerine yukarıdaki gibi print kullansaydık bunlar string olacağı ikin ikinci fonksiyonda hata alacaktık.
def üçleçarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a + 2
def dördeböl(a):
    print("3.fonksiyon çalıştı")
    return a / 4
# 3 ünü beraber kullanalım.

print(dördeböl(ikiyletopla(üçleçarp(5))))

#>>>>!!!!return ifadesinden sonra fonksiyonumuz tamamıyla sona erer. Yani, return ifadesinden sonra yapılan herhangi bir işlem çalıştırılmaz.
def toplama(a,b,c):
    return a + b + c
    print("Toplama fonksiyonu") # Çalıştırılmadı.
"""
"""""
#FONKSİYONLARDA PARAMETRE TÜRLERİ

#Biz eğer bir parametrenin değerini varsayılan olarak belirlemek istersek, bunu varsayılan değerler ile yapabiliriz. Varsayılan değerleri anlamak için selamla fonksiyonunu varsayılan parametre değeri ile yazalım.
def selamla(isim="İsimsiz"):
    print("İsminiz:",isim)

selamla() #!Varsayılan değer tanımlamasak bu kod hata verecekti
def bilgilerigöster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara =  "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgilerigöster("Kutay","Akpınar") # ad ve soyadı kendimiz verdik numara varsayılan değer oldu.
#Ancak böyle bir durumda argümanları gönderirken değerleri sıralı vermemiz gerekiyor. Peki sadece numara parametresine değer vermek istersek ne yapacağız ?
bilgilerigöster(numara = "123456") # numara parametresini özel olarak belirtiyoruz.
#Ad: Bilgi Yok Soyad: Bilgi Yok Numara: 123456
print("Mehmet","Kutay","Akpınar",sep = "/") # sep parametresine özel olarak değer atadık.
"""

#Fonksiyonlarda esnek değerler

"""def toplama(a,b,c):
    print(a+b+c)"""  #mesela bu fonksiyonumuzun içine 4 tane değer gönderirsek kod hata verecektir.
#bu yüzden şöyle yapabilriiz.
"""
def toplama(*parametreler): # Artık parametreler değişkenini bir demet gibi kullanabilirim.
    toplam =  0
    print("Parametreler:",parametreler)     #Parametreler: (1, 2, 3, 4, 5, 6)   verdiğim değerler tekli tuple oluşturdu.
    for i in parametreler:
        toplam += i
    return toplam
print(toplama(1,2,3,4,5,6 ))


print(toplama()) # boş tuple oluşturdum ve değerim 0 .

def carpma(*sayılar):
    total=1
    for i in sayılar:
        total *= i
    return total

print((carpma(1,2,3)))"""

#FONKSİYONLARDA GLOBAL VE YEREL DEĞİŞKENLER
""" Pythonda fonksiyonlarda tanımlanan değişkenler Python tarafından Yerel (Local) değişkenler olarak tanımlanırlar. Yani bir fonksiyon bloğunda oluşturulan değişkenler fonksiyona özgüdür ve fonksiyon çalışmasını bitirdikten sonra bu değişkenler bellekten silinir ve yok olur. Böylelikle , fonksiyon içinde tanımlanmış bir değişkene başka bir yerden erişilemez.

Pythonda en genel kapsama sahip değişkenler ise Global değişkenler olarak tanımlanırlar ve global değişkenlere tanımlandığı andan itibaren programın her yerinden ulaşabiliriz."""

"""
#YEREL DEĞİŞKEN
def fonksiyon():
    a=10
    print(a)

fonksiyon() # çıktısı :10
#print(a) bunu çalıştırısak hata verir çünkü a sadece fonksiyon içinde tanımlı.

#GLOBAL DEĞİŞKEN
b=20
def fonksiyon2():
    print(b)
fonksiyon2()

c = 10 # Globalde tanımlanmış bir değişken
def fonksiyon():
    c = 2 # Yerelde tanımlanmış bir değişken
    print(c)  # Yerel değişken kullanılıyor.

fonksiyon()
print(c)

#Peki bir fonksiyonda globalde tanımlanmış bir değişkeni nasıl kullanacağız ? Bunun için Pythonda global ifadesi bulunmaktadır. Şimdi aşağıdaki kodu beraber inceleyelim.

#Global Deyimi

d=5
def fonksiyon():
    global d
    d=3
    print(d) # artık globaldaki d değeri de 3 oldu

fonksiyon() # 3
print(d)  #3


#PEKİ IF VE WHILE İÇİNDEKİ DEĞİŞKENLER YEREL Mİ GLOBAL Mİ?

if True:
    e = 4
    print(e) # GLOBAL OLDU WHILE DA DA GLOBAL OLUR.
print(e)"""
#LAMBDA İFADELERİ

#lambda ifadeleri fonksiyonlarımızı oluşturmak için Pythonda bulunan pratik bir yöntemdir ve gerektiği yerlerde bu ifadeleri kullanabiliriz.

def ikiyleçarp(x): # Klasik fonksiyon tanımlama
    return x * 2


ikiyleçarp = lambda x : x * 2 # x parametre x* 2 return ifadesi ve ikiyleçarp değeri de bir etikettir(değişken gibi düşünelim)

def toplama(a,b,c):
    return a + b + c

topla = lambda x,y,z : x + y + z

def ters(s):
    return s[::-1]

terscev=lambda a : a[::-1]
print(terscev("kutay"))


#YANİ YAPI ŞU ŞEKİLDE
                        """  etiket = lambda parametre1,parametre2.... :  İşlem        """