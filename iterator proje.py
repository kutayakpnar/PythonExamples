class Kuvvet3():
    def __init__(self,max=0):
        self.max=max
        self.kuvvet=0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.kuvvet<=self.max):
            sonuc= 3**self.kuvvet
            self.kuvvet+=1

            return sonuc
        else:
            raise StopIteration

kuvet=Kuvvet3(6) #yani en fazla 3ün 6.kuvvetini görücez
iterator=iter(kuvet)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""
1
3
9
27
81
243
729

"""
