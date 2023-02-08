class Dosya():

    def __init__(self):
        with open("7.gündosyaişlemleriörnek.txt","r",encoding="utf-8") as file:
            dosya_iceriği=file.read()
            kelimeler=dosya_iceriği.split()
            self.sadekelimeler=list()
            for i in kelimeler:
                i=i.strip("\n")
                i=i.strip(" ")
                i=i.strip(".")
                i=i.strip(",")

                self.sadekelimeler.append(i)

    def tumkelimeler(self):
        kelimelerkumesi=set()

        for i in self.sadekelimeler:
            kelimelerkumesi.add(i)

        print("Tüm kelimeler:")
        for i in kelimelerkumesi:
            print(i)
            print("********")

    def kelimefrekansı(self):
        kelimesözlük=dict()
        for i in self.sadekelimeler:
            if (i in kelimesözlük):
                kelimesözlük[i]+=1
            else:
                kelimesözlük[i]=1

        for kelime,sayı in kelimesözlük.items() :
            print("{} kelimesi {} defa geçiyor.".format(kelime,sayı))
            print("---------------")




dosya=Dosya()
dosya.kelimefrekansı()



