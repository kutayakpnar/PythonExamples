import random
import time
print("""
*****1 ile 40 arasında bir sayı tahmin edin.*****
""")
rastgele_sayı=random.randint(1,40)   #bu şekilde 1 ile 40 arasında random bir sayı elde ederiz.
tahmin_hakkı=7

while True:
    tahmin = int(input("Bir sayı tahmin edin:"))
    if (tahmin < rastgele_sayı):
        print("Bilgiler sorgulanıyor..")
        time.sleep(1) #program çalışması 1 saniye bekleyecek.
        print("Daha yüksek bir sayı söyleyin.")
        tahmin_hakkı -= 1
    elif(tahmin > rastgele_sayı):
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)  # program çalışması 1 saniye bekleyecek.
        print("Daha düşük bir sayı söyleyin.")
        tahmin_hakkı -= 1
    else:
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)  # program çalışması 1 saniye bekleyecek.
        print("Tebrikler.Sayımız:",rastgele_sayı)
        break
    if(tahmin_hakkı== 0):
        print("Tahmin hakkınız bitti.Çıkış yapılıyor..")
        break


