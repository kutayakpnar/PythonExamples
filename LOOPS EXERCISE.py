"""
#Try to find out if a number you get from the user is perfect.

i=1
total=0
a=int(input("Please enter the number:"))
while (i<a):
    if (a%i == 0):
        total+=i
    i+=1

if (total == a):
    print("It is a perfect number.")
else:
    print("It is not a perfect number.") """


"""
#Try to find out if a number you received from the user is "Armstrong"
a=input("Please enter the number:")
basamaksayısı=len(a)
sayı=int(a)
basamak=0
toplam=0
x=sayı
while (x>0):
    basamak=x%10
    toplam += basamak**basamaksayısı
    x //=10

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")"""


#Try to print a multiplication table with numbers from 1 to 10.

"""
for i in range(1,11):
    print("*********")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))"""

"""
toplam=0
while True:
    a=input("Please enter the number if u want to exit click Q ")
    if(a=="Q"):
        break


    a = int(a)
    toplam+=a
    print(toplam)"""

"""
#Print only the numbers divisible by 3 from the numbers from 1 to 100. Try to do this with continue.

for i in range(1,101):
    if (i%3 != 0):
        continue
    print(i)
"""


x=[i for i in range(1,101) if (i%2 == 0)]
print(x)















