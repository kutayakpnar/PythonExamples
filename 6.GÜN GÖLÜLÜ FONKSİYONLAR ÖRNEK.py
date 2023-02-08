"""
#problem 1
liste=[(3, 4), (10, 3), (5, 6), (1, 9)]
def alan(demet):
    return demet[0]*demet[1]

a=list(map(alan,liste))
print(a)"""

"""
c=[(3,4,5),(6,8,10),(3,10,7)]
def üçgen_mi(demet):
    if (abs(demet[0] + demet[1]) > demet[2] and abs(demet[0] + demet[2]) > demet[1] and abs(demet[1] + demet[2]) >demet[0]):
        return True
    else:
        return False

a=list(filter(üçgen_mi,c))
print(a)"""

"""
a= [1,2,3,4,5,6,7,8,9,10]
def cift(x):
    if x%2 == 0:
        return True
    else:
        return False

b=list(filter(cift,a))
from functools import reduce
c=reduce(lambda x,y:x+y , b)
print(c)"""

isimler =["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisimler =["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

x=list(zip(isimler,soyisimler))
for i,j in x:
    print(i,j)


