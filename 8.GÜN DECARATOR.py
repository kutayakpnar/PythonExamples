"""
*args ve **kwargs
Fonksiyonlara argüman göndermenin esnek bir şekilde yapıldığını biliyoruz. İsterseniz ilk olarak yıldızlı argümanları hatırlamaya çalışalım."""



def fonksiyon(*args):
    for i in args:              #yani istediğimiz sayıda argüman gönderebiliccez.gönderdiğimiz argümanlar fonksiyonda demet haline dönüşecek.
        print(i)

fonksiyon(1,2,3,4)

def fonksiyon2(isim,*args):
    print("İsim:",isim)
    print("*********")
    for i in args:
        print(i)

fonksiyon2("Kutay",12,34,56)

# *kwarg argümanlara isim vererek göndermemizi sağlar.

def fonksiyon3(**kwargs): #kwargs sözlük oluştutur.
    print(kwargs)

fonksiyon3(isim="kutay",soyisim="akpınar",numara=123)  #çıktı : {'isim': 'kutay', 'soyisim': 'akpınar', 'numara': 123}
# peki kwags üzeride nasıl gezinebilirim?

def fonksiyon4(**kwargs): #kwargs sözlük oluştutur.
    for i,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)

fonksiyon4(isim="kutay",soyisim="akpınar",numara=123)

""" Argüman İsmi: isim Argüman Değeri: kutay
Argüman İsmi: soyisim Argüman Değeri: akpınar
Argüman İsmi: numara Argüman Değeri: 123 """

def fonksiyon5(*args,**kwargs):
    for i in args:
        print(i)
    print("******************")
    for i,j in kwargs.items():
        print(i,j)


fonksiyon5(1,2,3,4,5,6,7,8,isim="kutay",soyisim="akpınar",numara=123)      #sayılar args yerine geçer geri kalan kwargs

#İç içe fonksiyonlar
#Pythonda fonksiyonlar da birer obje oldukları için
#hem bir tane değişkene atanabilirler, hem de başka bir fonksiyonun içinde tanımlanabilirler. Şimdi bunlara bakmaya başlayalım.

def selamla(isim):
    print("Selam",isim)

selamla("ayşe")

merhaba = selamla
#yani merhaba objesini selamla fonksiyonuna eşitledik merhaba da artık bir fonksiyon
merhaba("Kutay") #artık bunu selamla fonksiyonu  gibi kullanabilirim.
# çıktı Selam Kutay

#şimdi selamlayı siliyorum

del selamla #peki merhabaya nolacak

merhaba("çağla") #Selam çağla merhaba fonksiyonu silinmemiş


#iç  içe fonksiyonlar

def fonksiyon():

    def fonksiyon2():
        print("Küçük fonksiyondan herkese merhaba:")

    fonksiyon2()
    print("Büyük fonksiyondan herkese merhaba")

fonksiyon() #Küçük fonksiyondan herkese merhaba:
             #Büyük fonksiyondan herkese merhaba

#fonksiyon2() dersem hata alırım çünkü fonksiyon2 fonksiyon içinde local değişken

def fonksiyon8(*args):

    def toplama(x):
        toplam=0
        for i in x:
            toplam+=i
        return toplam
    print(toplama(args))

fonksiyon8(1,2,3,4,5,6)