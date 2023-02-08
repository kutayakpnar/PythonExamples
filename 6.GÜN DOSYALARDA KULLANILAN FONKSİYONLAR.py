#Dosyaları Otomatik Kapatma

#Bunun için Pythonda dosyalarda işimiz bitince otomatik kapatma özelliği bulunuyor. Bundan sonra Pythonda dosya işlemlerimizi şu blok içinde yapacağız.
# with open(dosya_adı,dosya_kipi) as file:
                    #Dosya işlemleri

"""with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8") as file:
    for i in file:"
        print(i,end="")"""

#Dosyaları İleri Geri Sarmak
#Biliyorsunuz önceki dersimizde dosyaları okurken sadece dosyanın en başından başlayabiliyorduk ve dosya imlecimiz okuma işleminin sonunda , dosyanın en sonuna gidiyordu.
#Ancak biz çoğu zaman dosya imlecini (file) dosyanın herhangi bir yerine götürmek isteyebiliriz.
#Bunun için Pythondaki seek() fonksiyonunu kullanacağız. Ancak ondan önce dosya imlecinin hangi byteda olduğunu söyleyen tell() fonksiyonuna bakalım.

"""with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8") as file:
    print(file.tell())  #0 en baştayım yani 0. byteta
    file.seek(20) #imleci 20.byte gönderdim
    print(file.tell()) #çıktı:20"""

""" 
    with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8") as file:
    file.seek(5) #5.bytea gittim
    icerik=file.read(10) #şu an 5.bytedayım ve buradan itibaren 10 byte oku dedim.
    print(icerik) # çıktı:n,Java,C,P"""

with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r",encoding="utf-8") as file:
    file.seek(5) #5.bytea gittim
    icerik=file.read(10) #şu an 5.bytedayım ve buradan itibaren 10 byte oku dedim.
    print(file.tell())
    print(icerik)  # çıktı:n,Java,C,P
    file.seek(0) #imlecimi en başa gönderdim
    icerik2=file.read(6)
    print(file.tell())
    print(icerik2) # çıktı: Python


