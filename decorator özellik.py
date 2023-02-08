def ekstra(func):
    def wrapper(sayılar):
        ciftlertoplamı=0
        ciftsayılar=0
        teklertoplamı=0
        teksaılar=0
        for sayı in sayılar:
            if (sayı%2==0):
                ciftlertoplamı+=sayı
                ciftsayılar+=1
            else:
                teklertoplamı+=sayı
                teksaılar+=1
        print("Teklerin ortalaması:",teklertoplamı/teksaılar)
        print("Çiftlerin ortalaması:",ciftlertoplamı/ciftsayılar)

        func(sayılar)

    return wrapper


@ekstra
def ortalamabul(sayılar):
    toplam=0
    for i in sayılar:
        toplam +=i
    print("Genel ortalma:",toplam/len(sayılar))

ortalamabul([1,23,4,56,7,6,45,65,654,6,546,54,6,54,76,87,9,66,7534,534,54,346,63])
