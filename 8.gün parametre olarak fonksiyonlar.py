#Fonksiyonları Dönmek ve Argüman Olarak Göndermek
#Bu konuda fonksiyonları return ile başka bir fonksiyondan dönmeyi ve diğer fonksiyonlara parametre olarak göndermeyi öğreneceğiz.

#onksiyonları return ile Dönmek
#Bir fonksiyon aynı zamanda bir obje olduğu için, bu fonksiyonu başka bir fonksiyondan return ile döndürebiliriz.

def anafonksiyon(islemadı):

    def toplama(*args):
        toplam =0
        for i in args:
            toplam+=i
        return toplam
    def carpım(*args):
        x=1
        for i in args:
            x*=i
        return x

    if (islemadı=="toplama"):
        return toplama
    else:
        return carpım

fonk=anafonksiyon("toplama")
#fonk artık toplama fonksiyonunu döner
#fonku toplama ile kullanalım.
print(fonk(1,2,3,56,7)) #69

fonk2 = anafonksiyon("carpım")

print((fonk2(1,2,3,4))) #24

#Fonksiyonları Argüman Olarak Göndermek

def toplama(a,b):
    return a + b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a * b
def bölme(a,b):
    return a / b

def anafonksiyon(func1,func2,func3,func4,islemadı):
    if (islemadı=="toplama"):
        print(func1(2,5))
    elif (islemadı=="çıkarma"):
        print(func2(8,5))
    elif (islemadı=="çarpma"):
        print(func3(3,7))
    elif (islemadı=="bölme"):
        print(func4(20,5))
    else:
        print("geçersiz işlem")

anafonksiyon(toplama,çıkarma,çarpma,bölme,"toplama") # 7 5+2
anafonksiyon(toplama,çıkarma,çarpma,bölme,"çıkarma") # 3 8-5
anafonksiyon(toplama,çıkarma,çarpma,bölme,"çarpma") #21 3*7
anafonksiyon(toplama,çıkarma,çarpma,bölme,"bölme")  #4.0 20/5





