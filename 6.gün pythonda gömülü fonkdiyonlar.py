"""
#map fonksiyonu
#    map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)

def double(x):
    return x * 2

print(list((map(double,[1,2,3,4])))) #[2, 4, 6, 8] her bir eleman üstünde döner

list(map(double,(1,2,3,4,5,6,7))) #[2, 4, 6, 8, 10, 12, 14]

#Buradaki fonksiyonları lambda ifadeleriyle de yazabiliriz.

print(list(map(lambda x:x*3,[1,2,3])))  #[3, 6, 9]

#Map fonksiyonu birden fazla liste veya demet alabilir.
liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

print(list(map(lambda x,y : x * y , liste1,liste2))) #[5, 12, 21, 32]

list(map(lambda x,y,z : x * y * z , liste1,liste2,liste3))
#[45, 120, 231, 384]

"""
"""
#REDUCE FONKSİYONU
#reduce(function, iterasyon yapılabilen veritipi(liste vb.))
#reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular
#ve daha sonra çıkan sonucu listenin 3. elemanına uygular ve bu şekilde devam ederek liste bitince bir tane değer döneR

#REDUCE KULLANMAL İÇİN

from functools import reduce
def toplama(x,y):
    return x+y

print(reduce(toplama,[12,18,20,10])) #60

reduce(lambda x,y : x * y , [1,2,3,4,5]) #5in faktoriyelini bulur.

def maksimum(x,y):
    if x>y:
        return x
    else:
        return y

print(reduce(maksimum,[-2,3,4,7,5]))"""
"""
#FİLTER FONKSİYONU
           #   filter(fonksiyon,iterasyon yapılabilen bir veritipi(liste vb.))

#filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True , False) bir fonksiyon alır ve liste gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular.
#filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döner. Hemen örneklerimize bakalım.


print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))) #[2, 4, 6, 8, 10]

def asal_mi(x):
    i = 2
    if (x == 1):
        return False # Asal değil
    elif(x == 2):
        return True # Asal sayı
    else:
        while(i < x):
            if (x % i == 0):
                return False # Asal Değil
            i += 1
        return True

print(list(filter(asal_mi,range(1,100)))) # 1 den 100' e kadar olan asal sayılar.)
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]"""
""" 
#ZIP FONKSIYONU
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.
i=0
liste=list()
while (i<len(liste1) and i<len(liste2)):
    liste.append((liste1[i],liste2[i]))
    i+=1

print(liste)
#Peki böyle uzun bir işlemi zip fonksiyonuyla nasıl yaparız ? İsterseniz zip fonksiyonunun kullanımını direk örnek üzerinden görelim.

print(list(zip(liste1,liste2))) #sonç aynı

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = ["Python","Php","Java","Javascript","C"]

print(list(zip(liste1,liste2,liste3)))
#[(1, 5, 'Python'), (2, 6, 'Php'), (3, 7, 'Java'), (4, 8, 'Javascript')]

# Sözlükleri zipleyelim.
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}

list(zip(sözlük1,sözlük2)) # Anahtarlar eşleşti.#[('Elma', 'Sıfır'), ('Armut', 'Bir'), ('Kiraz', 'İki')]
list(zip(sözlük1.values(),sözlük2.values()))#değerler eşleşti  #[(1, 0), (2, 1), (3, 2)]"""

"""#ENUMERATE FONKSİYONU

liste = ["Elma", "Armut", "Muz", "Kiraz"]

# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuç = list()

i = 0

for a in liste:
    sonuç.append((i, a))
    i += 1
print(sonuç) #[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

#Yani aslında burada herbir elemanı indekslerle numaralandırıyor ve demet çiftleri oluşturuyoruz. for döngüsü yazarken bazen hem elemanları hem de indeksleri almak isteyebiliriz.
# Böyle bir durumda numaralandırma işlemi yapan enumerate fonksiyonunu kullanabiliriz.
liste = ["Elma","Armut","Muz","Kiraz"]
print(list(enumerate(liste))) #[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

liste = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste):
    if (index % 2 == 0):
        print("Eleman: ",eleman)
    #Eleman:  a
    #Eleman:  c
    #Eleman:  e
    #Eleman:  g"""

#ALL VE ANY FONKSİYONU
def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True


# Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
liste = [True, False, True, False, True]
liste = [1,2,3,4,5] # Daha önceden biliyoruz. 0' haricinde bütün sayılar True sayılmaktadır.

hepsi(liste) # Hepsi True

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
# Herhangi bir değer True ise True, Hepsi False ise False döndürmek istiyoruz.

liste = [True,False,True,False,True]
herhangi(liste) #TRUE

#Aslında bu işlemleri all() ve any() fonksiyonları yapmaktadır. İsterseniz bunların örneklerine bakalım.

#all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürüR

liste = [True,False,True,False,True]
all(liste)
False
liste = [1,2,3,4,5]
all(liste)
True
any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.

liste = [True,False,True,False,True]
any(liste)
True
liste = [0,0,0,0,0,0,0]
any(liste)
False
İşte bu kadar ! all ve any fonksiyonlarını bu tarz işlemler yaparken kullanabilirsiniz.




