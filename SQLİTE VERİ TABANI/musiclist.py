import sqlite3
class sarkı():
    def __init__(self,sarkıadı,sanatcı,sarkısüresi):
        self.sarkıadı=sarkıadı
        self.sanatcı=sanatcı
        self.sarkısüresi=sarkısüresi
        print("******")

    def __str__(self):
        return "Şarkı Adı:{}\nSanatçı:{}\nŞarkı Süresi:{}\n".format(self.sarkıadı,self.sanatcı,self.sarkısüresi)



class Library():
    def __init__(self):
        self.baglantıolustur()


    def baglantıolustur(self):
        self.baglantı=sqlite3.connect("Library.db")
        self.cursor=self.baglantı.cursor()
        sorgu="create table if not exists musiclist (isim TEXT,sanatçı TEXT,sarkısüresi INT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()

    def baglantıkes(self):
        self.baglantı.close()

    def sarkılarıgöster(self):
        sorgu="select * from musiclist"
        self.cursor.execute(sorgu)
        sarkılar=self.cursor.fetchall()
        if (len(sarkılar)==0):
            print("Şarkı listesi boş.")

        else:
            for i in sarkılar:
                sarkıx=sarkı(i[0],i[1],i[2])
                print(sarkıx)

    def sarkısorgula(self,sarkı2):
        sorgu= "Select * from musiclist where isim=?"
        self.cursor.execute(sorgu,(sarkı2,))
        x=self.cursor.fetchall()

        if(len(x)==0):
            print("Böyle bir şarkı yok")
        else:

            sarkıx=sarkı(x[0][0],x[0][1],x[0][2])

            print(sarkıx)


    def sarkıekle(self,sarkı):
        sorgu = "Insert into musiclist Values(?,?,?)"
        self.cursor.execute(sorgu,(sarkı.sarkıadı,sarkı.sanatcı,sarkı.sarkısüresi))
        self.baglantı.commit()

    def toplamsarkısüresi(self):
        sorgu = "select * from musiclist"
        self.cursor.execute(sorgu)
        sarkılar = self.cursor.fetchall()
        x=0

        for i in sarkılar:
            print(i)
            x += i[2]
        print(x)




