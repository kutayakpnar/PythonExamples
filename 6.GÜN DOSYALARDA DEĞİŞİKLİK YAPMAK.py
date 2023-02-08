#R+ KİPİ hem dosyayı okumamızı hemde dosyaya yazmamızı sağlar.

"""
with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r+",encoding="utf-8") as file:
    file.seek(10)
    file.write("DENEME") #MEHMET KUTDENEMEPINAR
                          İZMİR YÜKSEK
                           TEKNOLOJİ
                           BURHANİYE """


#DOSYANIN SONUNDA DEĞİŞİKLİK YAPMAK a kipi ile açarız ve ensona gider.
""" with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","a",encoding="utf-8") as file:
    file.write("ören\n")  #en sona ekledim"""

"""
#Dosyanın başında değişilik yapmak:
with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r+",encoding="utf-8") as file:
    icerik=file.read()
    icerik = "Başa ekledimi?\n" + icerik
    file.seek(0)
    file.write(icerik)"""

#DOSYANIN ORTASINDA DEĞİŞİKLİK YAPMAK

#Dosyaların ortasına herhangi bir satır eklemek için ilk olarak her bir satırı liste halinde almamızı sağlayan readlines() fonksiyonunu kullanacağız.
#Daha sonra bu listenin herhangi bir yerine bir eleman ekleyerek bu listeyi for döngüsü ile dosyaya yazacağız.

""" with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r+",encoding="utf-8") as file:
    liste=file.readlines() #her bir eleman bir satır
    liste.insert(3,"ÖREN\n") #listemin 3.indeksine ören eklemeye çalışıyorum
    file.seek(0)
    for i in liste:
        file.write(i)"""

#for döngüsü kullanmak yerine writelines fonksiyonu da kullanabiliriz.

with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r+",encoding="utf-8") as file:
    liste=file.readlines() #her bir eleman bir satır
    liste.insert(3,"ÖREN\n") #listemin 3.indeksine ören eklemeye çalışıyorum
    file.seek(0)
    file.writelines(liste)

with open("bilgilerPYTHON6.GÜNDOSYALAR.txt","r+",encoding="utf-8") as file:
    print(file.read())

