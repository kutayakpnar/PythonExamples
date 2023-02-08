import sqlite3
import time

class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):
        self.isim=isim
        self.yazar=yazar
        self.yayınevi=yayınevi
        self.tür=tür
        self.baskı=baskı

    def __str__(self):
        return "Kitap İsmi:{}\nYazar:{}\nYayınevi:{}\nTür:{}\nBaskı:{}".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)

class Kütüphane():
    def __init__(self):
        self.baglantı_olustur()

    def baglantı_olustur(self):
        self.baglantı=sqlite3.connect("kütüphane2.db")
        self.cursor=self.baglantı.cursor()
        sorgu="Create table if not exists kitaplar (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Tür Text,Baskı INT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()

    def bağlantıyıkes(self):
        self.baglantı.close()

    def kitaplarıgöster(self):
        sorgu= "select * from kitaplar"
        self.cursor.execute(sorgu)
        kitaplar=self.cursor.fetchall()
        if (len(kitaplar)==0):
            print("Kütüphanede Kitap bulunmamaktadır.")

        else:
            for i in kitaplar:
                kitap=Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitapsorgula(self,isim):
        sorgu= "select * from kitaplar where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if (len(kitaplar)==0):
            print("Böyle bir kitap bulunmuyor.")
        else:
            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def kitapekle(self,kitap):
        sorgu="insert into kitaplar values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))

        self.baglantı.commit()

    def kitapsil(self,isim):
        sorgu="Delete from kitaplar where isim =?"
        self.cursor.execute(sorgu,(isim,))
        self.baglantı.commit()

    def baskıyükselt(self,isim):
        sorgu="select * from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if (len(kitaplar)==0):
            print("Böyle bir kitap bulunmuyor.")
        else:
            baskı = kitaplar[0][4]
            baskı +=1
            sorgu2="update kitaplar set baskı=? where isim=?"
            self.cursor.execute(sorgu2(baskı,isim))
            self.baglantı.commit()