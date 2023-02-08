#INHERITANCE KALITIM
#Inheritance veya kalıtım bir sınıfın başka bir sınıftan özelliklerini(attribute ) ve metodlarını miras almasıdır.
class Çalışan():
    def __init__(self, isim, maaş, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")

        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim, self.maaş, self.departman))

    def departman_degistir(self, yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman

#Çalışan sınıfını oluşturduk şimdi de Yönetici sınıfını bu Çalışan sınıfından türetmeye çalışalım.

class Yönetici(Çalışan): # Çalışan sınıfından miras alıyoruz. Miras aldığımız için parantez içini boş bırakmadık doldurduk.
    pass # Pass Deyimi bir bloğu sonradan tanımlamak istediğimizde kullanılan bir deyimdi.Bunu koymazsan sıkıntı çıkar
  #Artık yönetici sınıfı çalışan sınıfının bütün özellik ve metodlarına sahip oldu.Kontrol edelim.

yönetici1 = Yönetici("Mehmet Baltacı",3000,"İnsan Kaynakları") # yönetici objesi
# bunu çalıştırınca çıktı : Çalışan sınıfının init fonksiyonu

print(yönetici1.bilgilerigoster())

#Peki biz Yönetici sınıfına ekstra fonksiyonlar ve özellikler ekleyebiliyor muyuz ? Örnek olması açısından zam_yap isimli bir metod ekleyelim.

class Yönetici(Çalışan):
    def zamyap(self,zammiktarı):
        self.maaş += zammiktarı

yönetici2 = Yönetici("Mustafa Murat Coşkun",3000,"Bilişim") # yönetici objesi
yönetici2.zamyap(50)
print(yönetici2.bilgilerigoster()) #Çalışan sınıfının init fonksiyonu
                                    #Çalışan sınıfının bilgileri.....
                                    #İsim : Mustafa Murat Coşkun
                                    #Maaş: 3050
                                    #Departman: Bilişim


#Overriding (İptal Etme) !!!!!!!!!!!!!!!
#Eğer biz miras aldığımız metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak , artık metodu çağırdığımız zaman miras aldığımız değil kendi metodumuz çalışacaktır.
# Buna Nesne Tabanlı Programlamada bir metodu override etmek denmektedir.

class Çalışan():
    def __init__(self, isim, maaş, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")

        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim, self.maaş, self.departman))

    def departman_degistir(self, yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman


class Yönetici(Çalışan):

    def __init__(self, isim, maaş, departman, kişi_sayısı):  # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı  # Yeni eklenen özellik

    def zam_yap(self, zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı

a = Yönetici("Mustafa Murat Coşkun",3000,"Bilişim",10) # Yönetici sınıfının init fonksiyonu. Override edildi.
print(a.bilgilerigoster())


#super Anahtar Kelimesi  super().__init__(istenilenler)

#super anahtar kelimesi özellikle override ettiğimiz bir metodun içinde aynı zamanda miras aldığımız bir metodu kullanmak istersek kullanılabilir.
#Yani super en genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan kullanmamızı sağlar. Hemen örnek üzerinden anlamaya çalışalım.

class Çalışan():
    def __init__(self, isim, maaş, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")

        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim, self.maaş, self.departman))

    def departman_degistir(self, yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman


class Yönetici(Çalışan):

    def __init__(self, isim, maaş, departman, kişi_sayısı):  # Sorumlu olduğu kişi sayısı
        super().__init__(isim, maaş, departman)  # 3 tane özelliği Çalışan fonksiyonunun init fonksiyonuyla hallediyoruz. super().__init__(istenilenler)

        print("Yönetici sınıfının init fonksiyonu")

        self.kişi_sayısı = kişi_sayısı  # Ekstra özelliği de kendimiz yazıyoruz.

    def bilgilerigoster(self):
        print("Yönetici sınıfının bilgileri.....")

        print(
            "İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim, self.maaş, self.departman, self.kişi_sayısı))

    def zam_yap(self, zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı
c = Yönetici("Oğuz Artıran",3000,"İnsan Kaynakları",4) #Çalışan sınıfının init fonksiyonu
                                                       #Yönetici sınıfının init fonksiyonu      YANİ İKİ İNİT FONKSİYONU DA ÇALIŞTI!

