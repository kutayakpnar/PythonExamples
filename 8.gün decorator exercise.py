def ekstra(func):
    def mukemmel():
        print("Mükemmel sayılar.")
        for sayı in range(2,1001):
            toplam=0
            x=1
            while(x<sayı):
                if (sayı%x == 0):
                    toplam+=x
                x+=1
            if (toplam == sayı):
                print(sayı)
        func()
    return mukemmel()

@ekstra
def asal():

    for sayı in range(2,1001):
        toplam = 0
        x = 2
        while(x < sayı):
            if (sayı%x==0):
                toplam+=1
            x+=1
        if (toplam==0):
            print(sayı)








