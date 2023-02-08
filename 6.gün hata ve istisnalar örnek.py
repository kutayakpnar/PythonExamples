"""
liste = ["345","sadas","324a","14","kemal"]

for i in liste:
    try:
        print(int(i))
    except:
        pass"""

def ciftmi(sayı):

    if(sayı%2==0):
        return sayı
    else:
        raise ValueError

liste=[1,2,3,4,5,6]
for i in liste:
    try:
        ciftmi(i)
        print(i)
    except:
        pass







