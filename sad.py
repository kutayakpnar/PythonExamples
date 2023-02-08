def asal(sayı):
    if (sayı==1 or sayı==2):
        print("Bu bir asal sayıdır.")

   elif:
        toplam = 0
        for i in range(2, sayı):

            x = 2
            while (x < i):
                if (sayı % x == 0):
                    toplam += 1
                x += 1
        if (toplam == 0):

        print("Bu bir asal sayıdır.")





while True:
    a=input("Sayı:")
    if (a == "q"):
        break
    else:
        a=int(a)
        asal(a)
