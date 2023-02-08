#Nesne Tabanlı Programlama - Metodlar
#Burada bir sınıf içinde metodlarımızı nasıl tanımlayacağımızı öğrenmeye çalışacağız. Bunun için ilk olarak bir Yazılımcı sınıfı tanımlayalım.

class yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maaş=maaş
        self.diller=diller

# yazılımcı1 objesi
yazılımcı1 =  yazılımcı("Mustafa Murat","Coşkun",12345,3000,["Python","C","Java"])
yazılımcı2 = yazılımcı("Serhat","Say",23456,3500,["Matlab","R","SmallTalk"])

print(yazılımcı1.diller)
print(yazılımcı2.maaş)

#Önceki dersten bunların nasıl yapıldığını biliyoruz. Peki bu class'a metodlarımızı nasıl tanımlayabiliriz ? '
#Aynı init metodunu tanımladığımız gibi bir class'a da istediğimiz kadar metod tanımlayabiliriz.
#Örneğin ,Yazılımcı classına bilgilerigöster isimli bir metod tanımlayalım. yani bu metodlar aslında bir fonksiyon
class Yazılımcı():

    def __init__(self, isim, soyisim, numara, maaş, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara  # Yazılımcı objelerinin özellikleri
        self.maaş = maaş
        self.diller = diller

    def bilgilerigöster(self):
        print("""
        İSİM :{}
        SOYİSİM :{}
        NUMARA:{}
        MAAŞ:{}
        DİLLER:{}""".format(self.isim,self.soyisim,self.numara,self.maaş,self.diller)) #formatlarken de self ile formatladık

yazılımcı1 =  Yazılımcı("Mustafa Murat","Coşkun",12345,3000,["Python","C","Java"])
print(yazılımcı1.bilgilerigöster())

#Burada bilgilerigöster isimli metod tanımlayarak her bir özelliğimizin değeri ekrana derli toplu bir şekilde yazdırmış olduk.
# Metodlarımızı yazarken dikkat etmemiz gerek nokta, her metodun birinci parametresinin self referansı olması gerektiğidir.
# Ayrıca objelerimizin özelliklerine mutlaka self referansıyla erişmemiz gerekiyor. İsterseniz bu classa 2 tane daha metod yazalım.

class Yazılımcı():

    def __init__(self, isim, soyisim, numara, maaş, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara  # Yazılımcı objelerinin özellikleri
        self.maaş = maaş
        self.diller = diller

    def bilgilerigöster(self):
        print("""
        İSİM :{}
        SOYİSİM :{}
        NUMARA:{}
        MAAŞ:{}
        DİLLER:{}""".format(self.isim,self.soyisim,self.numara,self.maaş,self.diller)) #formatlarken de self ile formatladık

    def dilekle(self,yenidil):
        print("Dil ekleniyor.")
        self.diller.append(yenidil)

    def maasyukselt(self,zam):
        print("zam yapılıyor")
        self.maaş+= zam

yazılımcı1 =  Yazılımcı("Mustafa Murat","Coşkun",12345,3000,["Python","C","Java"])
yazılımcı1.dilekle("kutayakpınar")
print(yazılımcı1.bilgilerigöster())
yazılımcı1.maasyukselt(352)
print(yazılımcı1.bilgilerigöster())
