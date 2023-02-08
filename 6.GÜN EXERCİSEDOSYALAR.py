def not_hesaplama(satır):


    satır = satır[:-1]

    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):

        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"



with open("6.GÜNEXERCİSEDOSYA.txt","r+",encoding="utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        print(i)
        x= i.split(",")
        print(x)

        eklenecekler_listesi.append(not_hesaplama(i))

    with open("6.GÜNEXERCİSENOTLAR.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)
    kalanlar=[]
    geçenler=[]
    for i in eklenecekler_listesi:
        i=i[:-1]
        print(i)
        if (i[-1]=="F" or i[-2]=="F" or i[-2]=="D" ):
            kalanlar.append(i)
        else:
            geçenler.append(i)



    with open ("6.GÜNKALANLARLİSTESİ.txt","w",encoding = "utf-8") as file3:
        for i in kalanlar:
            file3.write(i +"\n")







    with open("6.GÜNgeçenler.txt", "w", encoding="utf-8") as file4:
        for i in geçenler:
            file4.write(i+"\n")