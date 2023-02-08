#Problem 1
#Print perfect numbers from 1 to 1000 on the screen. Write a function for this that returns whether a number is perfect or not.

"""
def mukemmel(sayı):
    total = 0
    for i in range(1,sayı):
        if (sayı%i==0):
            total +=i
    if (total == sayı):
        return True
    else:
        return False


while True:
    a=input("Please enter the number:")
    if (a=="q"):
        break

    else:
        a = int(a)
        if mukemmel(a):
            print(a,"is a perfect number.")
        else:
            print(a,"is not a perfect number.")
**************************************************"""

"""
def mukemmel(sayı):
    total = 0
    for i in range(1,sayı):
        if (sayı%i==0):
            total +=i
    return total == sayı

for i in range(2,1001):
    if (mukemmel(i)):
        print("Mükemmel sayı:",i)"""

#Problem 2
#Write a function that takes 2 numbers from the user and returns the greatest common divisor (EBOB) of these numbers.

"""def ebob(x,y):
    liste=list()
    if (x>=y):
        for i in range(1,y+1):
            if (x%i == 0 and y%i==0):
                liste.append(i)
    else:
        for i in range(1,x+1):
            if (x%i == 0 and y%i==0):
                liste.append(i)
    return liste[-1]


while True:
    a=input("Please enter the number 1:")
    b=input("Please enter the number 2:")
    if (a=="q" or b == "q"):
        break
    else:
        a=int(a)
        b=int(b)
        print("Ebob of these numbers is:",ebob(a,b))"""

"""
def ebob(x,y):
    i = 1
    ebob=1
    while(i<=x and i <=y):
        if(x%i==0 and y%i==0):
            ebob = i
        i +=1
    return ebob
x = int(input("Sayı-1:"))
y = int(input("Sayı-2:"))

print("Ebob:",ebob(x,y))"""


"""
def ekok_bulma(sayı1, sayı2):
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i == 0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok
sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:",ekok_bulma(sayı1,sayı2))"""


"""
birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
def sayıokuma(x):
    ondalık = x//10
    birlik = x%10
    return onlar[ondalık]+" "+ birler[birlik]

a = int(input("Lütfen sayıyı girin:"))
print(sayıokuma(a))"""

def pisagor():
    liste=list()
    for i in range(1,101):
        for j in range(1,101):
            c = (i ** 2 + j ** 2) ** 0.5
            if (c == int(c)):
                liste.append((i,j,int(c)))

    return liste

print(pisagor())

