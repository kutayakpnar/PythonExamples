""" Decorator Fonksiyonların Oluşturulması ve Kullanılması
Bu konuda decorator konseptini anlamaya çalışacağız.

Decorator fonksiyonlar, Pythonda fonksiyonlarımıza dinamik olarak ekstra özellik eklediğimiz fonksiyonlardır ve decorator
fonksiyonların kullanımı kod tekrarı yapmamızı engeller.
Pythonda decorator fonksiyonlar Flask gibi frameworklerde oldukça fazla kullanılır."""
import time
"""
def karelerihesapla(sayılar):
    sonuc=list()
    baslama=time.time() # for dögüsü başlamadan önceki zamanı verir.
    for i in sayılar:
        sonuc.append(i**2)
    bitis=time.time()
    print("bu fonksiyon"+ str(bitis-baslama)+"saniye sürdü.")
    return sonuc

def küplerihesapla(sayılar):
    sonuc = list()
    baslama = time.time()  # for dögüsü başlamadan önceki zamanı verir.
    for i in sayılar:
        sonuc.append(i ** 3)
    bitis = time.time()
    print("bu fonksiyon" + str(bitis - baslama) + "saniye sürdü.")
    return sonuc
karelerihesapla(range(100000))
küplerihesapla(range(100000))"""

def zamanhesapla(fonksiyon):
    def wrapper(sayılar):
        baslama = time.time()
        sonuç = fonksiyon(sayılar)
        bitis = time.time()
        print(fonksiyon.__name__ + " " + str(bitis - baslama) + " saniye sürdü.")
        return sonuç

    return wrapper
# zaman hesaplamayı kod tekrarına düşmek için iki fonksiyondada decoratör olarak kullanıcaz.
@zamanhesapla # zaman hesapla kareleri hesaplanın dekoratörü oldu
def karelerihesapla(sayılar):
    sonuc=list()

    for i in sayılar:
        sonuc.append(i**2)
    bitis=time.time()

    return sonuc
@zamanhesapla #zaman hesapla küpleri hesaplanın dekoratörü oldu.
def küplerihesapla(sayılar):
    sonuc = list()

    for i in sayılar:
        sonuc.append(i ** 3)
    bitis = time.time()

    return sonuc
karelerihesapla(range(100000))
küplerihesapla(range(100000))


