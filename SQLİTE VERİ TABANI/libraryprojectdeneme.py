from LIBRARYPROJECT  import *

print("""************************
Kütüphane Programına Hoşgeldiniz.
İşlemler;
1.Kitapları Göster
2.Kitap Sorgulama
3.Kitap Ekle
4.Kitap Sil
5.Baskı Yükselt
Çıkmak İçin 'q'ya basınız.
*****************""")

kütüphane=Kütüphane()


while True:
    işlem = input("Lütfen işlemi giriniz:")
    if (işlem=="q"):
        print("Yine Bekleriz..")
        break
    elif(işlem == "1"):

        kütüphane.kitaplarıgöster()

    elif (işlem == "2"):
        isim=input("Hangi kitap?")
        kütüphane.kitapsorgula(isim)

    elif (işlem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı"))

        yenikitap=Kitap(isim,yazar,yayınevi,tür,baskı)

        kütüphane.kitapekle(yenikitap)
        print("Kitap eklendi.")
    elif (işlem == "4"):
        isim=input("Hangi kitabı silmek istiyorsunuz?")
        kütüphane.kitapsil(isim)
        print("Kitap silindi.")


    elif (işlem == "5"):
        isim=input("Hangi kitabın baskısını yükseltmek istiyorsunuz?")
        kütüphane.baskıyükselt(isim)

        print("Baskı yükseltildi.")
    else:
        print("Geçersiz İşlem")

