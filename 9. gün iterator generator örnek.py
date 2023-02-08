"""
 class Kareler():
    def __init__(self,maks=0):
        self.maks=maks
        self.kuvvet=1

    def __iter__(self):
        return self
    def __next__(self):
        if(self.kuvvet<=self.maks):
            x=self.kuvvet**2
            self.kuvvet+=1

            return x

        else:
            raise StopIteration

kareler=Kareler(5)
iteration=iter(kareler)
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))"""

def asal(sayı):
    i=2
    while(i<sayı):
        if (sayı%i ==0):
            return False
        i+=1
    return True
def asalgen():
    i=2
    while True:
        if(asal(i)):
            yield i

        i+=1
for sayı in asalgen():
    if (sayı>1000):
        break
    print(sayı)


