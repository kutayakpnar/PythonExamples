

class pc():
    def __init__(self,marka="Monster",Ram=8,SSD=512):
        self.marka=marka
        self.Ram=Ram
        self.SSD=SSD

    def __str__(self):
        return "Marka:{}\nRam:{}\nSSD:{}".format(self.marka,self.Ram,self.SSD)

    def __len__(self):
        return self.Ram

    def ramgüncelle(self,x):
        self.Ram += x
    def ssdarttır(self,y):
        self.SSD+=y

bilgisayar=pc()

print("""
1.Bilgileri Göster
2.Boyutu göter
3.Ram arrtır
4.SSD arttır
5.Çıkış """)

while True:
    işlem=input("İşlem Seçiniz:")
    if (işlem == "5"):
        break
    elif(işlem =="1"):
        print(bilgisayar)
    elif(işlem=="2"):
        print(len(bilgisayar))

    elif(işlem == "3"):
        x=int(input("Ne kadar arttırmak istersin:"))
        bilgisayar.ramgüncelle(x)
    elif (işlem == "4"):
        x = int(input("Ne kadar arttırmak istersin:"))
        bilgisayar.ssdarttır(x)

    else:
        print("Lütfen geçerli bir işlem giriniz.")









