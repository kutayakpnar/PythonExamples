#Dosya Açmak
#Bir dosyayı açmak için open() fonksiyonunu kullanıyoruz. Yapısı şu şekildedir;

                #open(dosya_adı,dosya_erişme_kipi)

#"w" dosya kipi
#Dosyalarımızı açmak ve dosyalarımıza yazmak için "write" anlamına gelen "w" kipini kullanıyoruz. "w" kipi eğer oluşturmak istediğimiz dizinde öyle bir dosya yoksa dosyayı oluşturuyor , eğer öyle bir dosya varsa dosyayı silip tekrar oluşturuyor.
#Yani, eğer açmak istediğimiz dosyadan zaten varsa ve dosyanın içi doluysa "w" kipi dosyadaki bilgileri silip tekrar oluşturacaktır. (Biraz Tehlikeli)

"""open("bilgilerPYTHON6.GÜNDOSYALAR.txt","w") # Dosyayı bulunduğumuz dizinde açıyor"""
"""file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","w")  # Dosya üzerinde işlem yapacak dosya imlecini file isimli değişkene atıyoruz.
#Dosyaları Kapatmak
#Bir dosya üzerinde işlem yaptığımızda o dosyayı kapatmak sistem kaynaklarının gereksiz kullanılmaması açısından önemlidir.
#Çünkü programımız bitse bile dosyanın kapanacağı garanti değildir. Bu yüzden işlerimiz bittiği zaman dosyayı kapatmalıyız.
file.close()"""

"""
file=open("C:/Users/kutay/Desktop/PYTHONDOSYALAR6.GÜNÖRNEK.txt","w")
#programlamada 1 karakter 1 bytedır.
file.close()"""

"""
file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","w",encoding="utf-8")
file.write("Mehmet Kutay Akpınar")
file.close()
file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","w",encoding="utf-8")
file.close() #yeniden oluşurdum dosya boş """

#a kipi ile dosyaya yazma

#"a" Kipiyle Dosyalara Yazmak
#"append" (ekleme) kelimesinin kısaltması olan "a" kipiyle bir dosyayı açtığımızda , dosya eğer yoksa oluşturulur.
#Eğer öyle bir dosya mevcut ise, dosya tekrar oluşturulmaz ve dosya imleci dosyanın sonuna giderek dosyaya ekleme yapmamızı sağlar>1imlecin sonu

""" file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","a",encoding="utf-8")
file.write("Mehmet Kutay Akpınar")
file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","a",encoding="utf-8")
file.write("İzmir Yüksek Teknoloji Enstitüsü")
file.close()"""
"""
file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","a",encoding="utf-8")
file.write("Mehmet Kutay Akpınar\n")
file.write("İYTE")
file.close()"""

#DOSYA OKUMA İŞLEMLERİ
# OKUMAK İÇİN "r" kipi kullanırız.

#Dosyaları okumak ve verileri almak için "r" kipiyle açmamız gerekiyor. "r" kipiyle açtığımız dosya eğer bulunmuyorsa "FileNotFoundError" hatası dönecektir.
#Şimdi bulunduğumuz dizinde bulunan "bilgiler.txt" dosyasını açalım.
"""file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8")
file.close()"""

#file = open("bilgiler2.txt","r",encoding="utf-8")  # böyle bir dosya yok . O yüzden FileNotFoundError hatası döndü.

""" try:
    file = open("bilgiler2.txt","r",encoding= "utf-8")
except FileNotFoundError:
    print("Dosya Bulunamadı....")
Dosya Bulunamadı...."""                #Dosya işlemlerini daha güvenli yazmak try,except bloklarını kullanabilirsiniz.,

#Peki bir dosyanın içinden bilgileri nasıl okuyacağız ? Bunun için Pythonda değişik yöntemler bulunuyor. İsterseniz bu yöntemleri tek tek görmeye çalışalım.

""" file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8") #file imleci dosyanın içindeki imlec gibi düşün
for i in file: #tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    print(i) # Her bir satırı ekrana basıyoruz.
file.close()"""

#çıktıda her bir satır arasında fazladan boşluk çıktı çünkü pythonda her i den sonra endisi bir \n koyuyor.
#bunu engellemek için

""" file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8") #file imleci dosyanın içindeki imlec gibi düşün
for i in file: #tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    print(i,end="") # Her bir satırı ekrana basıyoruz. #end= ile sonuna \n koyma hiçbir şey koyma dedik
file.close()
 #şimdi çıktımız dosyadaki gibi aynen bastırıldı"""

#read() fonksiyonu
#read() fonksiyonu eğer içine hiçbir değer vermezsek bütün dosyamızı okuyacaktır.

"""
file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8")
icerik=file.read()
print("içerik:\n",icerik,sep="")
file.close()
#ve artık imlecim sona gitti .İkinci defa okumak istersem çıktıda bişey yazmaz çünkü imlecim sonda."""
#readline() fonksiyonu
#readline() fonksiyonu her çağrıldığında dosyanın sadece bir satırını okur. Her seferinde dosya imlecimiz (file) bir satır atlayarak devam eder.

"""
file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8")
print(file.readline())  #ilk 2 satırı okudum ve aralarına python kendisi boşluk koydu.
print(file.readline())
file.close()"""


#readlines() fonksiyonu
#readlines() fonksiyonu dosyanın bütün satırları bir liste şeklinde döner.

file=open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8")
print(file.readlines())
file.close()
