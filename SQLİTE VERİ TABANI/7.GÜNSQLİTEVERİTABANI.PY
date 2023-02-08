import sqlite3

con=sqlite3.connect("kütüphane.db") #veri tabanımızı uzantısı db olmalı oluşturmak için sqlite3.connect komutu kullanıyoruz.
#yoksa oluşturur ve bağlanır varsa sadece bağlanır
cursor= con.cursor() #bağlantı üzerinde bir tane imleç oluşturdum.
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT) ")
    #imleci kullanıp execute yazıyoruz ve içine sorgumuzu string halinde yazıyoruz
    con.commit() #veri tabanı üzerinde yukarıdaki sorgunun etkili olması için bağlantıyı commitlememiz lazım.
def veri_ekle():
    cursor.execute("insert into kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest Yayıncılık',561)")
    con.commit() # veri tabanı güncellenir.
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("insert into kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))#ULLANICIDAN ALACAĞIM DEĞERLERİ EKLEMEK İSTEDİĞİM İÇİN 4 TANE SORU İŞARETİ KOYDUM.
    con.commit()
def verileri_al():
    cursor.execute("Select * from kitaplık")
    liste = cursor.fetchall() #fetchall işlem yaptığımız cursor fonksiyonu üstündeki bütün bilgilerin bize dönmesini sağlar.
    #veritabanı üzerinde herhangi bir güncelleme yapmadığımız için . commit kullanmamıza gerek yok.
    print("Kitaplık Tablosunun Bilgileri:")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("select İsim,Yazar from kitaplık")
    liste=cursor.fetchall()
    for i in liste:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("select * from kitaplık where Yayınevi=?",(yayınevi,)) #tekdeğişkenli bile olsa sonuna virgül
    liste=cursor.fetchall()
    for i in liste:
        print(i)

def verilerigüncelle(eskiyayınevi,yeniyayınevi):
    cursor.execute("update kitaplık set yayınevi=? where yayınevi=?",(yeniyayınevi,eskiyayınevi))
    con.commit() #verileri güncelliycez o yüzden commit kullanmam lazım.

def verilerisil(yazar):
    cursor.execute("delete from kitaplık where yazar =?",(yazar,))
    con.commit()

verilerisil("Ahmet Ümit")



#isim=input("İsim:")
#yazar=input("Yazar:")
#yayınevi=input("Yayınevi:")
#sayfa_sayısı=int(input("Sayfa Sayısı:"))
#veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)
#verileri_al3("Everest")
con.close() #dosyalardaki gibi kapatmam lazım
"""
Kitaplık Tablosu oluşturma
Veritabanında kitaplık isimli bir tablo oluşturmak için şu 2 sorgudan birini kullanabiliriz.

CREATE TABLE kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT , Sayfa_Sayısı INT) - Bu sorgu kitaplık isimli bir tablo oluşturacak ve bu tablonun özellikleri İsim (TEXT --> String),Yazar(TEXT --> String),Yayınevi (TEXT ---> String), Sayfa_Sayısı(INT --- int) olacak. Ancak bu sorguyu arda arda çalıştırırsak "Tablo Already Exists" hatası alacağız.

CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT , Sayfa_Sayısı INT) - Bu sorgu tablo yoksa oluşturacak, tablo varsa hata vermeyecektir. Kodlarımız şu şekilde;
"""

#Şimdi de kitaplık tablomuza veri eklemeye çalışalım. Çalıştıracağımız sorgu şu olacak;

#INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)

#Not : SQL Sorguları büyük veya küçük harfle de yazılabilir. Örnek olarak

#insert into kitaplık values ('İstanbul Hatırası','Ahmet Ümit','Everest',561)

#Insert Into kitaplık Values ('İstanbul Hatırası','Ahmet Ümit','Everest',561)

#Peki kullanıcıdan aldığımız değerleri tabloya nasıl ekliyoruz ? Onun için de sorgumuzu ve kodumuzu biraz değiştireceğiz.

"""
Tablodaki Verileri Çekme
Önceki derslerimizde Tablo oluşturmayı ve Tabloya veri eklemeyi öğrenmiştik. Bu derste de tablodaki verileri nasıl çekeceğimizi öğrenmeye çalışacağız. Tablodan veri çekmek için şu SQL sorgularını kullanacağız.

Select * From kitaplık - Tablodaki tüm bilgileri almamızı sağlar.

Select İsim,Yazar From kitaplık Tablodaki tüm bilgileri sadece İsim ve Yazar özelliklerini almamızı sağlar.

Select * From kitaplık where Yayınevi = 'Everest' Sadece Yayınevi özelliği Everest olanları alır.

Şimdi isterseniz ilk sorgumuzu çalıştırdığımız kodumuzu yazalım."""

#Verileri Güncelleme
#Tablodaki verileri güncelleme için şöyle bir sorgu kullanabiliriz.

#Update kitaplık set Yayınevi = 'Everest' where Yayınevi = 'Doğan Kitap' -- Yayınevi 'Doğan Kitap' olan kitapların Yayınevi bilgilerini 'Everest' e günceller.

#Şimdi isterseniz bu sorguyu çalıştırdığımız kodumuzu yazalım.

"""
Tablodaki verileri silme için şöyle bir sorgu kullanabiliriz.

Delete From kitaplık where Yazar = 'Ahmet Ümit' -- Yazar özelliği 'Ahmet Ümit' olan kitapları tablodan siler.

Şimdi isterseniz bu sorguyu çalıştırdığımız kodumuzu yazalım."""