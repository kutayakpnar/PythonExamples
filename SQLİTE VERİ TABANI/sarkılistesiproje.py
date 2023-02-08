from musiclist import *

print("""**********
Music List
*********
İşlemler:
1-Şarkıları Göster
2-Şarkı Sorgula
3-Sarkı Ekle
4-Toplam Şarkı Süresi
Çıkmak İçin 'q'ya basınız.
*********
""")
sarkı1=Library()
while True:
    islem=input("Lütfen gerçekleştirmek istediğiniz işlemi girin:")
    if(islem=="q"):
        break
    elif(islem=="1"):
        sarkı1.sarkılarıgöster()
    elif(islem == "2"):
        sarkı2=input("İstediğiniz şarkı ismini giriniz:")
        sarkı1.sarkısorgula(sarkı2)
    elif(islem=="3"):
        sarkıadı = input("İsim:")
        sanatcı = input("Sanatçı:")
        sarkısüresi = int(input("Şarkı Süresi:"))
        yenisarkı=sarkı(sarkıadı,sanatcı,sarkısüresi)
        sarkı1.sarkıekle(yenisarkı)
        print("Şarkı eklendi.")

    elif(islem=="4"):
        sarkı1.toplamsarkısüresi()

print(yenisarkı.sanatcı())