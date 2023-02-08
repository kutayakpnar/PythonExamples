#OOP ÖZEL METODLAR:

class Kitap():
    pass

kitap= Kitap() # __init__ metodu çağrılıyor.
print(kitap)
#len(kitap) #hata verir çünkü len metodu tanımlı değil.

del kitap #kitap objesi silinir


#init metodu
#init metodunu kendimiz tanımlarsak artık kendi init fonksiyonumuz çalışacaktır.

class Kitap():
    def __init__(self,isim,yazar,sayfasayısı,tür):
        print("Kitap objesi oluşturuluyor")
        self.isim=isim
        self.yazar=yazar
        self.sayfasayısı=sayfasayısı
        self.tür=tür

kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye") # Kendi metodumuz

#str metodu
#Normalde print(kitap1) ifadesi ekrana şöyle bir yazı yazdırıyor.:<__main__.Kitap object at 0x000000CEE886EAC8>
#Ancak eğer str metodunu kendimiz tanımlarsak artık ekrana kitap1 in içeriğini daha anlaşılır yazabileceğiz.

class Kitap():
    def __init__(self,isim,yazar,sayfasayısı,tür):
        print("Kitap objesi oluşturuluyor")
        self.isim=isim
        self.yazar=yazar
        self.sayfasayısı=sayfasayısı
        self.tür=tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim:{}\nYazar:{}\nSayfa Sayısı:{}\nTür:{}".format(self.isim,self.yazar,self.sayfasayısı,self.tür)

kitap2 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap2)


#len metodu
#len metodu normalde özel olarak biz tanımlamazsak tanımlanan bir metod değil. Onun için bu metodu kendimiz tanımlamamız gereklidir.

class Kitap():
    def __init__(self,isim,yazar,sayfasayısı,tür):
        print("Kitap objesi oluşturuluyor")
        self.isim=isim
        self.yazar=yazar
        self.sayfasayısı=sayfasayısı
        self.tür=tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim:{}\nYazar:{}\nSayfa Sayısı:{}\nTür:{}".format(self.isim,self.yazar,self.sayfasayısı,self.tür)
    def __len__(self):
        return self.sayfasayısı
kitap2 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")

print(len(kitap2)) #561

#del metodu
#del metodu Pythonda bir objeyi del anahtar kelimesiyle sildiğimiz zaman çalıştırılan metoddur. Bu metodu kendimiz tanımlayarak ekstra özellikler ekleyebiliriz.

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
    def __del__(self):
        print("Kitap objesi siliniyor.......")



kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
"""del kitap1  # Ekstra ekrana yazdırma özelliği ekledik.
#Kitap objesi siliniyor......."""

"""
Siz de bunlar gibi çoğu özel metodu ihtiyacınız olduğu zaman kendiniz yazabilirsiniz. Özel metodlar için güzel bir ingilizce kaynak için şuradan faydalanabilirsiniz.

https://www.diveinto.org/python3/special-method-names.html
"""