#Generatorların Oluşturulması ve Kullanılması

"""
Generatorlar Pythonda iterable objeler (örnek olarak fonksiyonlar) oluşturmak için kullanılan objelerdir ve bellekte herhangi bir yer kaplamazlar.
 Örneğin, 100.000 tane değer üretip, bu değerleri bir listede tutmak bellekte oldukça fazla yer kaplayacaktır.
 O yüzden bu işlemi gerçekleştiren bir fonksiyonu generator fonksiyon şeklinde yazmak oldukça mantıklı olacaktır.
 Generatorları anlamak için isterseniz bir fonksiyonu ilk olarak generator kullanmadan yazmaya çalışalım.

"""

"""
def karelerial():
    sonuç = []

    for i in range(1, 6):
        sonuç.append(i ** 2)
    return sonuç


print(karelerial())
#[1, 4, 9, 16, 25]
#İsterseniz bu fonksiyonu bir de generator kullanarak yazmaya çalışalım. Generatorlerin değer üretmesi için yield anahtar kelimesini kullanacağız.

def karelerial2():
    for i in range(1,6):
        yield i**2        #yield kullanırız

generator=karelerial2()
print(generator) #<generator object karelerial2 at 0x0000023321BE6F90>
#peki değerleri nasıl alıcaz?
#bu değerler biz onlara ulaşmak istediğimizde üretilir.
iterator=iter(generator)
print(next(iterator)) #yield değer üretir 1in karesi
print(next(iterator)) #4 2 nin karesi 1 artık tarih oldu
print(next(iterator))#9 3ü n karesi 4 tarih oldu
print(next(iterator))
print(next(iterator))#16 9 tarih oldu tarih olan değerlere artık ulaşamam.

#bu değerleri bir daha elde edemeyeceğimizi görelim

iterator2=iter(generator)
print(next(iterator2)) #StopIteration hatası
#çünkü generatorım bu değerleri üretti ve işi bitti generatorun yeniden kullanılması için yeniden tanımlanması gerek"""


#Peki list compherensionu generatora nasıl çevirebilirim?

liste = [i * 3 for i in range(5)]
liste
#[0, 3, 6, 9, 12]

#=

generator=(i*3 for i in range(5))
print(generator) #<generator object <genexpr> at 0x0000018CD8686F90>

iterator=iter(generator)
print(next(iterator)) #0
print(next(iterator)) #3
print(next(iterator))  #6

"""
def carpımtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i, j, i * j)


for i in carpımtablosu():
    print(i)
#eğer böyle olmasaydı tüm değerleri bir listede saklardık""" 

for i in range(1,11):
    for j in range(1,11):
        print("{} x {} = {}".format(i, j, i * j))




