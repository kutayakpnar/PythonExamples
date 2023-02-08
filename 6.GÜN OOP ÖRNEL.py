#KUMANDA SINIFI GELİŞTİRME
import random
import time

class kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["trt"],kanal = "trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tvac(self):
        if (self.tv_durum=="Açık"):
            print("tv zaten açık")

        else:
            print("Tv açılıyor")
            self.tv_durum="Açık"

    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı..")
        else:
            print("Televizyon Kapanıyor....")
            self.tv_durum = "Kapalı"

    def sesayarları(self):
        while True:

            cevap=input("Sesi azalt:<\nSesi yükselt :>\Çıkış:çıkış")
            if (cevap == "<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses:",self.tv_ses)

            elif (cevap == ">"):
                if (self.tv_ses!=31):
                    self.tv_ses+=1

                    print("Ses:", self.tv_ses)

            else:
                print("Ses güncellendi")
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor.")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")

    def rastgele_kanal(self):
        rastgele= random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu:{}\nTv Ses:{}\nKanal Listesi:{}\nŞu anki kanal:{}\n.".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda=kumanda()
print("""
************TELEVİZYON KUMANDASI**********
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri
Çıkmak için 'q' ya basın.
""")

while True:
    işlem=input("İşlemi seçin:")
    if(işlem == "q"):
        print("Program kapatılıyor")
        break

    elif (işlem == "1"):
        kumanda.tvac()
    elif (işlem =="2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.sesayarları()

    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")
        kanallistesi=kanal_isimleri.split(",")
        for eklenecekler in kanallistesi:
            kumanda.kanal_ekle(eklenecekler)

    elif (işlem == "5"):

        print("Kanal Sayısı:", len(kumanda))

    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)

    else:
        print("Geçersiz İşlem......")
        




