"""
Iteratorlar aslında Pythonda çoğu yerde biz görmesek de kullanılır. Iteratorlar özellikle for döngülerinde , list comprehensionlarında,
 ve bir sonraki derste göreceğimiz generatorlarda karşımıza çıkar.
 Iteratorlar en genel anlamıyla üzerinde gezinilebilecek bir objedir ve bu obje her seferinde bir tane eleman döner.
 Pythonda kendisinden iterator oluşturabileceğimiz her obje iterable bir objedir.. Örneğin, demetlerden,listelerden
  ve stringlerden oluşturduğumuz bütün objeler iterable bir objedir.
  Bir objenin iterable olması için hazır metodlar olan __iter()__ ve __next()__ metodlarını mutlaka tanımlaması gerekir.
"""

#Iterator oluşturma
#Bir iterator objesini , iterable bir objeden (liste,demet,string vs) oluşturmak için Pythonda iter()
#fonksiyonunu kullanıyoruz ve bu objenin bir sonraki elemanını almak için next() fonksiyonu kullanıyoruz.
liste=[1,2,3,4,5]
print(dir(liste))

iterator=iter(liste) #bu liste üzerinde vir tane iterator objem oluşmuş oldu
print(iterator)  #<list_iterator object at 0x0000021909626BB0>
#iterator üzerinden elemnalara ulaşmak için:
print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3
print(next(iterator)) #4
print(next(iterator)) #5
#print(next(iterator))  #StopIteration hata çünkü bitti
#Aslında for döngülerinin iç yapısı şu şekildedir;

liste = [1,2,3,4,5]

iterator = iter(liste)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

"""
Kendi Iterable Objelerimizi Oluşturmak
Peki biz kendi oluşturduğumuz veritiplerini nasıl iterable yapacağız ? Bunun için oluşturacağımız sınıfların mutlaka
 __iter()__ ve __next()__ metodlarını tanımlaması gereklidir. Şimdi bir tane kumanda sınıfı oluşturalım ve bu sınıfı iterable yapalım.
"""
class Kumanda():
    def __init__(self,kanallistesi):
        self.kanallistesi=kanallistesi
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if (self.index < len(self.kanallistesi)):
            return self.kanallistesi[self.index]
        else:
            self.index=-1
            raise StopIteration

kumanda=Kumanda(["atv","fox,","kanald","startv","tv8"])
iterator=iter(kumanda)
print(next(iterator)) #atv (ilk eleman geldi)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator)) #hata

for i in kumanda:
    print(i)      #normalde hata verirdi artık vermiyor.çünkü defte iter ve nexti tamamladık.
    