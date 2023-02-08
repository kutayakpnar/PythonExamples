"""

a="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
liste=a.strip("")
kelimesayısı=dict()
for i in liste:
    if (i in kelimesayısı):
        kelimesayısı[i]+=1


    else:
        kelimesayısı[i]=1



for kelime,sayı in kelimesayısı.items():
    print("{} harfi {} defa geçiyor.".format(kelime,sayı))
    print("********")"""

"""
basharfler=""
with open("şiir7.günexercise.txt","r",encoding="utf-8") as file:
    for i in file:
        basharfler+=i[0]

print(basharfler)"""
isim =["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste=list(zip(isim,soyisim))
liste.sort()
for i,j in liste:
    print(i,j)





