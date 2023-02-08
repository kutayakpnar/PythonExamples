#SINIFLAR - CLASS
#Sınıflar veya Classlar objelerimizi oluştururken objelerin özelliklerini ve metodlarını tanımladığımız bir yapıdır ve biz herbir objeyi bu yapıya göre üretiriz. İsterseniz bir Araba classı tanımlayarak yapımızı kurmaya başlayalım.

class Araba():
    model = "renault megane"
    renk ="gümüş"
    beygir_gücü = 110
    silindir = 4                     #bunlar classımızın özellikleri (attributes)

#Sınıfımızı Pythonda tanımladık. Peki bu sınıftan obje nasıl oluşturacağız ? Bunu da şu şekilde yapabiliyoruz.

#obje_ismi = Sınıf_İsmi(parametreler(opsiyonel)

araba1=Araba() #araba1 =  Araba() # Araba veri tipinden bir "araba1" isminde bir obje oluşturduk.
print(type(araba1)) #<class '__main__.Araba'> veri tipimiz araba
#araba1 objesi artık sınıfta tanımladığımız bütün özelliklere (attributes) sahip olmuş oldu. İşte sınıf ve obje üretmek bu şekilde olmaktadır. Peki bu araba objesinin özelliklerinin nasıl görebiliriz ?

print(araba1.model)   #renault megane
print(araba1.renk)     #gümüş
print(araba1.beygir_gücü)  #110
print(araba1.silindir)    #4


#Burda gördüğümüz gibi oluşturduğumuz objelerin buradaki model,renk vs. gibi özelliklerinin değeri aynıdır. Çünkü aslında burada tanımladığımız özellikler birer sınıf özelliğidir. Yani biz bir obje oluşturduğumuzda bu özelliklerin değerleri varsayılan olarak gelir. Bu özelliklerin değerlerine , herhangi bir obje oluşturmadan da erişebiliriz. Bunu da şu şekilde yapabiliriz.

print(Araba.renk) #gümüş # Class_İsmi.özellik_ismi

#Bizim her bir objeyi başlangıçta farklı değerlerle oluşturmamız için her bir objeyi oluştururken objelerin değerlerini göndermemiz gerekiyor.
#Bunun için de özel bir metodu kullanmamız gerekmektedir.

            # __init__()

#Aslında init metodu Pythonda yapıcı(constructor ) fonksiyon olarak tanımlanmaktadır. Bu metod objelerimiz oluşturulurken otomatik olarak ilk çağrılan fonksiyondur.
#Bu metodu özel olarak tanımlayarak objelerimizi farklı değerlerle oluşturabiliriz.

# Araba Veri tipi

class Araba():
    # Şimdilik Class özelliklerine ihtiyacımız yok.

    def __init__(self):
        print("init fonksiyonu çağrıldı.")
araba1 = Araba() # araba1 objesi oluşurken otomatik olarak __init__ metodumuz çağrılıyor.

#self anahtar kelimesi objeyi oluşturduğumuz zaman o objeyi gösteren bir referanstır ve metodlarımızda en başta bulunması gereken bir parametredir.
#Yani biz bir objenin bütün özelliklerini ve metodlarını bu referans üzerinden kullanabiliriz.
#Objeler oluşturulurken, Python bu referansı metodlara otomatik olarak kendisi gönderir. Özel olarak self referansını göndermemize gerek yoktur.
#init metodunu ve self'i iyi anlamak için objelerimize özellikler ekleyelim.

class araba():
    def __init__(self,model,renk,beygirgücü,silindir): # Parametrelerimizin değerlerini objelerimizi oluştururken göndereceğiz.
        self.model=model # self.özellik_ismi = parametre değeri şeklinde objemizin model özelliğine değeri atıyoruz.
        self.renk=renk  #self.özellik_ismi = parametre değeri şeklinde objemizin renk özelliğine değeri atıyoruz.
        self.beygirgücü=beygirgücü
        self.silindir=silindir


# araba1 objesini oluşturalım.
# Artık değerlerimizi göndererek objelerimizin özelliklerini istediğimiz değerle başlatabiliriz.

araba1=araba("megane","beyaz",140,4)
araba2=araba("bmw","siyah",160,6)


print(araba1.model) #megane
print(araba2.model) #bmw

#istersek init metodunu varsayılan değerlerle de yazabiliriz.

class araba():
    def __init__(self,model="bilgi yok",renk="bilgi yok",beygirgücü="bilgi yok",silindir=4 ): # Parametrelerimizin değerlerini objelerimizi oluştururken göndereceğiz.
        self.model=model # self.özellik_ismi = parametre değeri şeklinde objemizin model özelliğine değeri atıyoruz.
        self.renk=renk  #self.özellik_ismi = parametre değeri şeklinde objemizin renk özelliğine değeri atıyoruz.
        self.beygirgücü=beygirgücü
        self.silindir=silindir

araba3=araba(beygirgücü=180,model="mercedes")
print(araba3.model) #mercedes
print(araba3.renk) #bilgi yok